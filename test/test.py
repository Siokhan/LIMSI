import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv('export.csv', encoding = "ISO-8859-1", index_col='ID')
testdf = pd.read_csv('testdata.csv', encoding = "ISO-8859-1", index_col='ID')

df2 = df.loc[:,('filename', 'track', 'start', 'end', 'duration', 'Value')]
testdf2 = testdf.loc[:,('filename', 'track', 'start', 'end', 'duration', 'Value')]

df3 = df2.loc[(df2['track'] == "Gaze")]
testdf3 = testdf2.loc[(testdf2['track'] == "Gaze")]

print(df3.head())
print(testdf3) 

testdf3['check'] = np.where(testdf3.Value == df3.Value, 'valid', 'invalid')

print(testdf3)
