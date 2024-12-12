import pandas as pd
from google.cloud import storage

# Load the data
df = pd.read_csv('../data/netflix_titles.csv')

# 1. Remove duplicates
df.drop_duplicates(inplace=True)

# 2. Handle missing values
# Remove rows with missing values
df = df.dropna(subset=['date_added'])

# Fill missing values with 'Unknown'
df.fillna({'director': 'Unknown', 'cast': 'Unknown', 'country': 'Unknown',
           'rating': 'No Data', 'duration': 'No Data'}, inplace=True)

print("\nMissing values handled. Updated info:")
print(df.isnull().sum())

# 3. Stripping extra spaces
df['date_added'] = df['date_added'].str.strip()

# 4. Convert data types
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y')

# 5. Add a new column for further analysis
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['month_name_added'] = df['date_added'].dt.month_name()

# 6. Rename column:
df = df.rename(columns={'listed_in': 'genre'})

print('\nDataset Overview after cleaning:')
pd.set_option('display.max_colwidth', 10)
pd.set_option('display.max_columns', None)
print(df.head())

print('\nDataset Info after cleaning:')
print(df.info())

# Save cleaned data in JSON format
df.to_json('../data/cleaned_data.json', index=False)

print("\nData cleaning is done!")

# Upload the cleaned file to GCP
client = storage.Client()
bucket = client.bucket('netflix-eda')  # replace with your bucket name
blob = bucket.blob('cleaned_data.json')
blob.upload_from_filename('../data/cleaned_data.json')
