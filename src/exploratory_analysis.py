import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import datetime

path = '../data/results/'


def save_plot(plot_type, fig, filename, output_dir=path):
    """
  Saves the current plot figure based on its type.

  Args:
    plot_type: Type of plot (e.g., "bar", "pie", "line").
    fig: Matplotlib figure object containing the plot.
    filename: Name of the file to save.
    output_dir: Directory to save the plot.
  """

    os.makedirs(output_dir, exist_ok=True)

    extension_map = {
        "bar": "_bar.png",
        "pie": "_pie.png",
        "line": "_line.png",
    }

    output_path = os.path.join(output_dir, filename + extension_map.get(plot_type, '.png'))

    plt.savefig(output_path)
    plt.close(fig)


df = pd.read_json('../data/cleaned_data.json')


def set_common_plot_format(ax, title, xlabel='', ylabel='', rotation=0, fontsize=10):
    plt.title(title, fontsize=15)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    plt.xticks(rotation=rotation, fontsize=fontsize)


# 1. Genre analysis
genre_counts = df['genre'].str.split(', ').explode().value_counts()
genre_threshold = 0.01
threshold = genre_counts.sum() * genre_threshold
other_genres = genre_counts[genre_counts <= threshold].sum()
top_genres = genre_counts[genre_counts > threshold]
top_genres['Other'] = other_genres

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(ax=ax, x=top_genres.values, y=top_genres.index, orient='h', color='#e50914')

set_common_plot_format(ax, 'Most Popular Genres on Netflix', xlabel='Number of Movies and TV Shows')

plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=12)
plt.subplots_adjust(left=0.3)
save_plot('bar', fig, 'genre_analysis')

# 2. Country analysis
country_counts = df['country'].str.split(', ').explode().value_counts()
country_threshold = 0.015
threshold = country_counts.sum() * country_threshold
other_countries = country_counts[country_counts <= threshold]
other_countries = other_countries.sum()
country_counts = country_counts[country_counts > threshold]
country_counts['Other'] = other_countries
country_counts_percent = country_counts / country_counts.sum() * 100

palette = sns.color_palette('pastel')
fig, ax = plt.subplots(figsize=(12, 10))
ax.pie(country_counts, labels=country_counts.index, colors=palette, autopct='%1.1f%%', startangle=140,
       textprops={'fontsize': 14})
ax.set_title('Percentage of Movies and TV Shows by Country', pad=20, fontsize=20)
save_plot('pie', fig, 'country_analysis')

# 3. Year release analysis
release_year_data = df.groupby(['type', 'release_year']).size().unstack(fill_value=0)
range_years = 30
recent_years = release_year_data.loc[:, release_year_data.columns >= (datetime.date.today().year - range_years)]
total_by_type = recent_years.sum(axis=0)

fig, ax = plt.subplots(figsize=(15, 6))
sns.lineplot(data=recent_years.T, ax=ax)
plt.plot(total_by_type.index, total_by_type.values, label='Total', color='green')

set_common_plot_format(ax, 'Movies and TV Shows Released by Year', 'Release Year',
                       'Number of Movies and TV Shows')

plt.legend(title='Type', loc='upper left', fontsize='small')
plt.tight_layout()
plt.xticks(recent_years.columns, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
save_plot('line', fig, 'year_release_analysis')

# 4. Month added analysis
monthly_added_counts_by_type = df.groupby(['month_name_added', 'type']).size().reset_index(name='count')
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']
monthly_added_counts_by_type['month_name_added'] = pd.Categorical(monthly_added_counts_by_type['month_name_added'],
                                                                  categories=month_order, ordered=True)

palette = ['#221f1f', '#b20710']
fig, ax = plt.subplots(figsize=(18, 8))
sns.barplot(data=monthly_added_counts_by_type, x='month_name_added', y='count', hue='type', palette=palette, ax=ax)

set_common_plot_format(ax, 'Number of Movies and TV Shows Added by Month', '', '', 45)

plt.legend(title='Movie Type', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.subplots_adjust(left=0.1, right=0.8)
save_plot('bar', fig, 'month_added_analysis')

print(f'\nGraphics saved in: {path}')
