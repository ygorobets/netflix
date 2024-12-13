import pandas as pd
from google.cloud import storage

df = pd.read_csv('../data/netflix_titles.csv')

df_before_drop = df.copy()

df.drop_duplicates(inplace=True)

df.dropna(subset=['date_added'], inplace=True)

rows_deleted = len(df_before_drop) - len(df)
print(f"Deleted {rows_deleted} rows.")

df.fillna({'director': 'Unknown', 'cast': 'Unknown', 'country': 'Unknown',
           'rating': 'No Data', 'duration': 'No Data'}, inplace=True)

print("\nMissing values handled. Updated info:")
print(df.isnull().sum())

df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y')
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['month_name_added'] = df['date_added'].dt.month_name()

df = df.rename(columns={'listed_in': 'genre'})

print('\nDataset Overview after cleaning:')
pd.set_option('display.max_colwidth', 10)
pd.set_option('display.max_columns', None)
print(df.head())

print('\nDataset Info after cleaning:')
print(df.info())

df.to_json('../data/cleaned_data.json', index=False)

print('\nData cleaning is done!')

client = storage.Client()
bucket = client.bucket('netflix-eda')  # replace with your bucket name
blob = bucket.blob('cleaned_data.json')
blob.upload_from_filename('../data/cleaned_data.json')
print(f'\n{blob.name} was uploaded to {bucket.name} bucket!')
