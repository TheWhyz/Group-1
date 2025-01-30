import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# Load the CSV file
df = pd.read_csv("data/file_rootbeer.csv")

# Extract dates and authors from the 'Authors & Dates' column
date_list = []
file_indices = []
authors = []
unique_authors = set()

for i, row in df.iterrows():
    author_dates = row["Authors & Dates"].split("; ")
    for entry in author_dates:
        if "(" in entry and ")" in entry:
            author = entry.split(" (")[0]
            date_str = entry.split(" (")[1][:-1]  # Extract date string
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

            date_list.append(date_obj)
            file_indices.append(i)  # Use the index as x-axis value
            authors.append(author)
            unique_authors.add(author)

# Convert dates to weeks since the earliest commit
min_date = min(date_list)
weeks_since_start = [(d - min_date).days // 7 for d in date_list]

# Assign a unique color to each author
author_colors = {author: color for author, color in zip(unique_authors, plt.cm.rainbow(np.linspace(0, 1, len(unique_authors))))}

# Plot the scatterplot
plt.figure(figsize=(10, 6))

for i in range(len(file_indices)):
    plt.scatter(file_indices[i], weeks_since_start[i], color=author_colors[authors[i]], label=authors[i] if authors[i] not in plt.gca().get_legend_handles_labels()[1] else "")

# Labels and formatting
plt.xlabel("File Index")
plt.ylabel("Weeks Since First Commit")
plt.title("File Modification Timeline by Authors")
plt.legend(loc="upper right", fontsize="small", markerscale=1.2, ncol=2, frameon=True)
plt.grid(True, linestyle="--", alpha=0.6)

# Show the plot
plt.show()
