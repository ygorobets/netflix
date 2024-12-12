import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import datetime


def save_plot(plot_type, fig, filename, output_dir="../data/results/"):
    """
  Saves the current plot figure based on its type.

  Args:
    plot_type: Type of plot (e.g., "bar", "pie", "line").
    fig: Matplotlib figure object containing the plot.
    filename: Name of the file to save.
    output_dir: Directory to save the plot (default: "data/results").
  """

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    if plot_type == "bar":
        plt.savefig(os.path.join(output_dir, filename + "_bar.png"))
    elif plot_type == "pie":
        plt.savefig(os.path.join(output_dir, filename + "_pie.png"))
    elif plot_type == "line":
        plt.savefig(os.path.join(output_dir, filename + "_line.png"))
    else:
        plt.savefig(os.path.join(output_dir, filename + ".png"))
    plt.close(fig)


# Load the cleaned data
df = pd.read_json('../data/cleaned_data.json')

# 1. Genre analysis
genre_counts = df['genre'].str.split(', ').explode().value_counts()

# Set a threshold for "Other" genres (1% of total)
threshold = genre_counts.sum() * 0.01

# Create a new DataFrame with limited genres
other_genres = genre_counts[genre_counts <= threshold].sum()
top_genres = genre_counts[genre_counts > threshold]
top_genres['Other'] = other_genres

# Create a horizontal bar plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(ax=ax, x=top_genres.values, y=top_genres.index, orient='h', color='#e50914')
plt.title('Most Popular Genres on Netflix', fontsize=15)
plt.xlabel('')
plt.ylabel('')
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.subplots_adjust(left=0.3)
save_plot("bar", fig, "genre_analysis")

# 2. Country analysis
country_counts = df['country'].str.split(', ').explode().value_counts()

# Set a threshold for "Other" countries (1.5% of total)
threshold = country_counts.sum() * 0.015

# Create a new DataFrame with limited countries
other_countries = country_counts[country_counts <= threshold]
other_countries = other_countries.sum()
country_counts = country_counts[country_counts > threshold]
country_counts['Other'] = other_countries

# Calculate percentages for each country
country_counts_percent = country_counts / country_counts.sum() * 100

# Create a pie chart
palette = sns.color_palette("pastel")
fig, ax = plt.subplots(figsize=(12, 10))
ax.pie(country_counts, labels=country_counts.index, colors=palette, autopct='%1.1f%%', startangle=140,
       textprops={'fontsize': 14})
ax.set_title('Percentage of Movies and TV Shows by Country', pad=20, fontsize=20)
save_plot("pie", fig, "country_analysis")

# 3. Year release analysis
release_year_data = df.groupby(['type', 'release_year']).size().unstack(fill_value=0)
# Select a range of years (e.g., last 30 years) for a cleaner plot
recent_years = release_year_data.loc[:, release_year_data.columns >= (datetime.date.today().year - 30)]
total_by_type = recent_years.sum(axis=0)

# Create line plot
fig, ax = plt.subplots(figsize=(15, 6))
sns.lineplot(data=recent_years.T, ax=ax)
plt.plot(total_by_type.index, total_by_type.values, label='Total', color='green')
plt.title('Movies and TV Shows Released by Year', fontsize=15)
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.legend(title='Type', loc='upper left', fontsize='small')
plt.tight_layout()
plt.xticks(recent_years.columns, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
save_plot("line", fig, "year_release_analysis")

# 4. Month added analysis
monthly_added_counts_by_type = df.groupby(['month_name_added', 'type']).size().reset_index(name='count')

# Create bar plot
palette = ['#221f1f', '#b20710']
fig, ax = plt.subplots(figsize=(18, 8))
sns.barplot(data=monthly_added_counts_by_type, x='month_name_added', y='count', hue='type', palette=palette, ax=ax)
plt.title('Number of Movies and TV Shows Added by Month', fontsize=15)
plt.xlabel('')
plt.ylabel('')
plt.xticks(rotation=45)
plt.legend(title='Movie Type', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.subplots_adjust(left=0.1, right=0.8)
save_plot("bar", fig, "month_added_analysis")
