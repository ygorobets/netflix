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

df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), format='%B %d, %Y')
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


def upload_blob_to_gcs(bucket_name, source_file_path, destination_blob_name):
    storage_client = storage.Client()
    bucket_upload = storage_client.bucket(bucket_name)
    blob = bucket_upload.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)

    print(f"File {source_file_path} uploaded to {bucket_name} as {destination_blob_name}")


bucket = 'netflix-eda'
source_file = '../data/cleaned_data.json'
destination_blob = 'cleaned_data.json'

upload_blob_to_gcs(bucket, source_file, destination_blob)
