import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('data/file_rootbeer.csv')

# Extract necessary columns
filenames = df['Filename']
touches = df['Touches']
authors = df['Author']
timestamps = pd.to_datetime(df['Timestamp'])

# Convert timestamps to weeks since the earliest commit
min_date = timestamps.min()
weeks_since_start = ((timestamps - min_date).dt.days) // 7

# Assign a unique numeric ID to each filename for x-axis placement
unique_files = {file: idx for idx, file in enumerate(filenames.unique())}
file_indices = [unique_files[file] for file in filenames]

# Assign colors based on authors
authors_unique = df['Author'].unique()
author_colors = {author: plt.cm.tab10(i % 10) for i, author in enumerate(authors_unique)}
colors = [author_colors[author] for author in authors]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(file_indices, weeks_since_start, c=colors, alpha=0.7)

# Labels and title
plt.xlabel("file")
plt.ylabel("weeks")
plt.title("File Modifications Over Time")

# Create legend
legend_patches = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=author_colors[author], markersize=8, label=author) for author in authors_unique]
plt.legend(handles=legend_patches, title="Authors", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()