import pandas as pd
from pandas import DataFrame

df = pd.read_csv('export.csv', encoding = "ISO-8859-1", index_col='ID')
testdf = pd.read_csv('testdata.csv', encoding = "ISO-8859-1", index_col='ID')

df2 = df[['filename', 'track', 'start', 'end', 'duration', 'Value']]
testdf2 = testdf[['filename', 'track', 'start', 'end', 'duration', 'Value']]

print(df2.head())
print(testdf2.head())
