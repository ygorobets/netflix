# Netflix Exploration ![img.png](img.png)

## Description:

This project delves into a dataset of Netflix movies and TV shows, uncovering interesting insights about genres, ratings, countries, release years, monthly additions and more.

## Key Features:

* Analyzes genre distribution to identify the most popular genres on Netflix.
* Explores the origin of movies and TV shows by looking at the countries involved.
* Investigates trends in the number of movies and TV shows added to Netflix by year.
* Analyzes the distribution of movie and TV show additions by month throughout the year.
* Deeper analysis and visualization with interesting insights

## Requirements:

* Programming language: Python
* Tools: Git, Kaggle API, Google Cloud Storage, Jupyter

## Installation:

1. **Clone this Repository:**

Bash
```console
git clone https://github.com/ygorobets/netflix
cd netflix
```

2. **Install the Required Dependencies:**

Bash
```console
pip install -r requirements.txt
```

3. **Set up Kaggle API:**

* Create a Kaggle account (https://www.kaggle.com/) and go to your account settings.
* Create a new API token.
* Download the API token as a JSON file.
* Move the JSON file to your home directory (~/.kaggle/kaggle.json on Linux, OSX, and at C:\Users\<Windows-username>\.kaggle\kaggle.json on Windows)

4. **Download the Dataset:**

* Install the Kaggle API client:

Bash

```console
pip install kaggle
```
* Authenticate to Kaggle: Make sure you have the Kaggle API token in your home directory as kaggle.json.

* Run the script dataset_download.py to download dataset 

5. **Review the Downloaded Dataset:** 

Run the script data_overview.py to look at raw dataset 

6. **Clean Data and Download Updated Dataset to Google Cloud Storage:**

To upload your cleaned dataset to your Google Cloud Storage bucket, follow these simple steps:

* Make sure you're authenticated:

Bash

```console
gcloud auth application-default login
```
This will authenticate your local application with your Google Cloud account.

* Create 'netflix-eda' bucket in your Google Cloud Storage account or replace in the code with the actual name of your bucket.
* Run the script cleaning.py to clean the data and upload the updated file to the bucket on Google Cloud Storage

# Analysis and Visualisation:
Run the script exploratory_analysis.py.

This will generate plots and save them in the data/results directory.

**Results:**

The script creates four visualizations:

* genre_analysis.png: Shows the most popular genres on Netflix.
* country_analysis.png: Analyzes countries of origin for movies and TV shows.
* year_release_analysis.png: Explores trends in the number of movies and TV shows released by year.
* month_added_analysis.png: Visualizes the distribution of movie and TV show additions by month.

# Further Exploration:

You can find additional analysis and visualizations, as well as interesting insights in EDA.ipynb in the notebook directory.

This project provides a basic analysis of the Netflix data. 

Feel free to contribute to this project by adding more insights and visualizations.


# Author:

Yulia Gorobets