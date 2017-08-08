import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv('hussein.csv', encoding = "ISO-8859-1", index_col='framecounter')
veriteT = pd.read_csv('husseincompare.csv', encoding = "ISO-8859-1", index_col='framecounter')

#df2 = df.loc[:,('filename', 'track', 'start', 'end', 'duration', 'Value Right eye')]
#testdf2 = testdf.loc[:,('filename', 'track', 'start', 'end', 'duration', 'Value Left eye')]

#df3 = df2.loc[(df2['track'] == "Gaze")]
#testdf3 = testdf2.loc[(testdf2['track'] == "Gaze")]

#print(df3.head())
#print(testdf3) 

#testdf3['check'] = np.where(testdf3['Value'] == df3['Value'], 'valid', 'invalid')

#print(testdf3)

print(df.head())
print(veriteT)

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

#df['right #'] = np.where(df['Value Right eye'].str.contains('center, center'), '1')

#comparaison des valeurs à la verité terrain
if df['Value Right eye'].values.any() == 'center, center':
    df['right #'] = '1'
#elif df['Value Right eye'] == 'left, center':
 #   df['right #'] = '2'
#elif df['Value Right eye'] == 'left, Up':
 #   df['right #'] = '3'
#elif df['Value Right eye'] == 'center, Up':
 #   df['right #'] = '4'
#elif df['Value Right eye'] == 'right, Up':
 #   df['right #'] = '5'
#else:
 #   df['right #'] = '6'

print(df)
