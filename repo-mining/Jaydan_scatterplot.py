import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from datetime import datetime

df = pd.read_csv('data/authorTouched_rootbeer.csv')

# Convert Date column to datetime and expand multiple dates per row
df_exploded = df.assign(Date=df['Date'].str.split('; ')).explode('Date')
df_exploded['Date'] = pd.to_datetime(df_exploded['Date'])

# Convert dates to weeks since the earliest modification
min_date = df_exploded['Date'].min()
df_exploded['Weeks'] = ((df_exploded['Date'] - min_date).dt.days) // 7

# Assign numeric values to filenames for plotting
file_mapping = {file: idx for idx, file in enumerate(df_exploded['Filename'].unique())}
df_exploded['FileIndex'] = df_exploded['Filename'].map(file_mapping)

# Assign colors to authors
authors = df_exploded['Author'].unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(authors)))
author_colors = dict(zip(authors, colors))

# Plot scatter plot
plt.figure(figsize=(10, 6))
for author, color in author_colors.items():
    subset = df_exploded[df_exploded['Author'] == author]
    plt.scatter(subset['FileIndex'], subset['Weeks'], label=author, color=color, alpha=0.7)

# Formatting the plot
plt.xlabel("File")
plt.ylabel("Weeks")
plt.xticks(ticks=range(len(file_mapping)), labels=file_mapping.keys(), rotation=90)
plt.legend(title="Author", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the plot
plt.show()
