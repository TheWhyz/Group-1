import pandas as pd
import matplotlib.pyplot as plt

# load the CSV file
df = pd.read_csv('data/file_rootbeer.csv')

# get each column
filenames = df['Filename']
touches = df['Touches']
authors = df['Author']
timestamps = pd.to_datetime(df['Timestamp'])

# convert the timestamps to weeks
min_date = timestamps.min()
weeks_since_start = ((timestamps - min_date).dt.days) // 7

# give each file a unique number
unique_files = {file: idx for idx, file in enumerate(filenames.unique())}
file_indices = [unique_files[file] for file in filenames]

# assign each author a color
authors_unique = df['Author'].unique()
author_colors = {author: plt.cm.tab10(i % 10) for i, author in enumerate(authors_unique)}
colors = [author_colors[author] for author in authors]

# make the scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(file_indices, weeks_since_start, c=colors, alpha=0.7)
plt.xlabel("file")
plt.ylabel("weeks")
plt.title("File Modifications Over Time")

# legend
legend_patches = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=author_colors[author], markersize=8, label=author) for author in authors_unique]
plt.legend(handles=legend_patches, title="Authors", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()