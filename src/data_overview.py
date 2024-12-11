import pandas as pd

# Load the data
df = pd.read_csv('../data/netflix_titles.csv')

pd.set_option('display.max_colwidth', 10)
pd.set_option('display.max_columns', None)

print('\nDataset Overview:')
print(df.head())
print('\nDataset Info:')
print(df.info())
print('\nDataset Descriptive Data Statistics:')
print(df.describe())
print('\nMissing Values:')
print(df.isnull().sum())
print('\nDuplicates Values:')
print(df.duplicated().sum())
