import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = pd.read_csv('hussein.csv', encoding = "ISO-8859-1", index_col='framecounter')
veriteT = pd.read_csv('husseincompare.csv', encoding = "ISO-8859-1", index_col='framecounter')
symetryDf = pd.read_csv('symetry.csv', encoding = "ISO-8859-1", index_col='framecounter')
symetryDf.dropna(axis=0, how='any')

#df2 = df.loc[:,('filename', 'track', 'start', 'end', 'duration', 'Value Right eye')]
#testdf2 = testdf.loc[:,('filename', 'track', 'start', 'end', 'duration', 'Value Left eye')]
#df3 = df2.loc[(df2['track'] == "Gaze")]
#testdf3 = testdf2.loc[(testdf2['track'] == "Gaze")]
#testdf3['check'] = np.where(testdf3['Value'] == df3['Value'], 'valid', 'invalid')

print(df.head())
print(veriteT.head())

df['precision'] = np.where((df['Value Right eye'] == df['Value Left eye']), '1', '0') #1 means the reading is precise ie. both values are identical
print(df)
zeros = [(df[df.precision == '0'].shape[0])]
ones = [(df[df.precision == '1'].shape[0])]
print('nombre de valeurs incohérentes: ' + str(zeros))
print('nombre de valeurs cohérentes: ' + str(ones))

entries = len(df.index)

resultdf = pd.DataFrame({'Inconsistent':zeros, 'Consistent':ones, 'EntryNum':entries}, dtype=int)
precision = (resultdf.Consistent / resultdf.EntryNum) * 100
roundedprec = round(precision, 2)
print(resultdf)
print('Taux de détection  valid (%): ' + str(roundedprec))

df['Gaze#'] = 0

#assigne une valeur unique si Value Left et Right eye sont identique, facilitie comparaison a la verité terrain
conditions = [
        (df['Value Left eye'] == 'center, center') & (df['Value Right eye'] == 'center, center'),
        (df['Value Left eye'] == 'left, center') & (df['Value Right eye'] == 'left, center'),
        (df['Value Left eye'] == 'left, Up') & (df['Value Right eye'] == 'left, Up'),
        (df['Value Left eye'] == 'center, Up') & (df['Value Right eye'] == 'center, Up'),
        (df['Value Left eye'] == 'right, Up') & (df['Value Right eye'] == 'right, Up'),
        (df['Value Left eye'] == 'right, center') & (df['Value Right eye'] == 'right, center')]
choices = [1, 2, 3, 4, 5, 6]

conditions2 = [
        (veriteT['Value Left eye'] == 'center, center') & (veriteT['Value Right eye'] == 'center, center'),
        (veriteT['Value Left eye'] == 'left, center') & (veriteT['Value Right eye'] == 'left, center'),
        (veriteT['Value Left eye'] == 'left, Up') & (veriteT['Value Right eye'] == 'left, Up'),
        (veriteT['Value Left eye'] == 'center, Up') & (veriteT['Value Right eye'] == 'center, Up'),
        (veriteT['Value Left eye'] == 'right, Up') & (veriteT['Value Right eye'] == 'right, Up'),
        (veriteT['Value Left eye'] == 'right, center') & (veriteT['Value Right eye'] == 'right, center')]
choices2 = [1, 2, 3, 4, 5, 6]

veriteT['Gaze#'] = np.select(conditions2, choices2, default = 0)
df['Gaze#'] = np.select(conditions, choices, default = 0)

print(veriteT)

#comparaison des valeurs à la verité terrain
df['CmpVeriteT'] = np.where(df['Gaze#'] == veriteT['Gaze#'], 'correcte', 'incorrecte')
print(df)

#graphiques a barres qui visualise le nombre de resultats valid vs non valid
N = 3
width = 0.05
ind = np.arange(N)
fig, ax = plt.subplots()
plt.bar(ind,[resultdf.EntryNum,resultdf.Inconsistent,resultdf.Consistent])
plt.title('Nombre de resultats valid vs non-valid \nComparé au nombre totale de valeur')
plt.ylabel('Nombre de valeur')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('total', 'non-valid', 'valid'))

M = entries
ind2 = np.arange(M)
ind3 = ind2 + 1
df.plot(x=ind2, y='Gaze#')
plt.title('Frequence de valeurs valides')
plt.show()

#print(symetryDf)

df.to_csv('results.csv')
