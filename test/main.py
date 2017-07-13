import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv('hussein.csv', encoding = "ISO-8859-1", index_col='framecounter')
testdf = pd.read_csv('husseincompare.csv', encoding = "ISO-8859-1", index_col='framecounter')

#df2 = df.loc[:,('filename', 'track', 'start', 'end', 'duration', 'Value Right eye')]
#testdf2 = testdf.loc[:,('filename', 'track', 'start', 'end', 'duration', 'Value Left eye')]

#df3 = df2.loc[(df2['track'] == "Gaze")]
#testdf3 = testdf2.loc[(testdf2['track'] == "Gaze")]

#print(df3.head())
#print(testdf3) 

#testdf3['check'] = np.where(testdf3['Value'] == df3['Value'], 'valid', 'invalid')

#print(testdf3)

print(df.head())
print(testdf)

testdf['check1'] = np.where((testdf['Value Right eye'] == testdf['Value Left eye']), 'precise', 'not precise')

print(testdf)

#if df['Value Right eye'] == 'center, center':
 #   df['right #'] = '1'
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

