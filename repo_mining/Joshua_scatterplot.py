import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
from matplotlib import cm

# Load the CSV file
data_file = 'data/authors_file_rootbeer.csv'  # Ensure this is the correct path
df = pd.read_csv(data_file)

# Convert the 'Authors and Dates' column from JSON strings to lists
df['Authors and Dates'] = df['Authors and Dates'].apply(lambda x: json.loads(x) if isinstance(x, str) else [])

# Extract scatter plot data
scatter_data = []
for index, row in df.iterrows():
    filename = index  # Use index as the file ID
    for entry in row['Authors and Dates']:
        author, date = entry
        weeks = pd.to_datetime(date).to_period("W").ordinal  # Convert date to week number
        scatter_data.append((filename, weeks, author))

# Convert scatter_data into a DataFrame
scatter_df = pd.DataFrame(scatter_data, columns=['File', 'Weeks', 'Author'])

# Assign each author a unique color
authors = scatter_df['Author'].unique()
author_colors = {author: cm.get_cmap('tab10')(i % 10) for i, author in enumerate(authors)}

# Create the scatter plot
plt.figure(figsize=(10, 6))
for author in authors:
    author_df = scatter_df[scatter_df['Author'] == author]
    plt.scatter(author_df['File'], author_df['Weeks'], color=author_colors[author], alpha=0.7)

plt.xlabel("File")
plt.ylabel("Weeks")
plt.title("Authors' File Modification Activity Over Time")
plt.show()
