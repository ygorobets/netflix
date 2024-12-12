Title: Netflix Exploration: A Look at Movies and TV Shows

Description:

This project delves into a dataset of Netflix movies and TV shows, uncovering interesting insights about genres, countries of origin, release years, and monthly additions.

Key Features:

Analyzes genre distribution to identify the most popular genres on Netflix.
Explores the origin of movies and TV shows by looking at the countries involved.
Investigates trends in the number of movies and TV shows added to Netflix by year.
Analyzes the distribution of movie and TV show additions by month throughout the year.
Requirements:

Python 3.x
pandas
matplotlib
seaborn
Kaggle API
Installation:

Clone this repository:
Bash

git clone https://github.com/ygorobets/netflix
Navigate to the project directory:
Bash

cd netflix
Install required dependencies:
Bash

pip install pandas matplotlib seaborn kaggle
Set up Kaggle API:
Create a Kaggle account and go to your account settings.
Create a new API token.
Download the API token as a JSON file.
Move the JSON file to your home directory (usually ~) and rename it to kaggle.json.
Downloading the Dataset:

Install the Kaggle API client:
Bash

pip install kaggle
Authenticate to Kaggle: Make sure you have the Kaggle API token in your home directory as kaggle.json.
Download the dataset:
Bash

path = kagglehub.dataset_download('shivamb/netflix-shows')
Usage:

Replace the data path: Update the data path in the script to point to the downloaded dataset.
Run the script: python netflix_analysis.py (replace netflix_analysis.py with the actual script name if different)
This will generate plots and save them in the data/results directory.

Results:

The script creates four visualizations:

genre_analysis.png: Shows the most popular genres on Netflix.
country_analysis.png: Analyzes countries of origin for movies and TV shows.
year_added_analysis.png: Explores trends in the number of movies and TV shows added by year.
month_added_analysis.png: Visualizes the distribution of movie and TV show additions by month.
Further Exploration:

This project provides a basic analysis of the Netflix data. You can extend it by:

Analyzing ratings and user reviews.
Exploring relationships between genres and release years.
Investigating differences between movies and TV shows.
Feel free to contribute to this project by adding more insights and visualizations.

License:

This project is licensed under the MIT License (see LICENSE file for details).

Author:

Yulia Gorobets