import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Load data from the CSV file
csv_file = 'data/authors_rootbeer.csv'  # Replace with your file path
data = pd.read_csv(csv_file)

# Convert date strings to datetime objects
data['Date'] = pd.to_datetime(data['Date'])

# Calculate weeks since the start of the project
project_start_date = data['Date'].min()
data['Weeks'] = data['Date'].apply(lambda x: (x - project_start_date).days // 7)

# Assign a unique numerical index to each file for plotting
file_indices = {file: idx for idx, file in enumerate(data['Filename'].unique())}
data['FileIndex'] = data['Filename'].map(file_indices)

# Assign a unique color to each author
authors = data['Author'].unique()
author_colors = {author: plt.cm.get_cmap('tab10')(i % 10) for i, author in enumerate(authors)}

# Create the scatter plot
plt.figure(figsize=(8, 6))
for author in authors:
    author_data = data[data['Author'] == author]
    plt.scatter(
        author_data['FileIndex'],
        author_data['Weeks'],
        label=author,
        color=author_colors[author],
        alpha=0.8,
        s=50
    )

# Customize the plot
plt.xlabel('file')
plt.ylabel('weeks')
plt.title('Weeks vs Files Touched')
plt.xticks(range(len(file_indices)), labels=list(file_indices.values()), rotation=0)
plt.grid(True, linestyle='--', alpha=0.5)

# Legend outside the plot
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1), title='Authors', fontsize='small', ncol=1)
plt.tight_layout()

# Show or save the plot
plt.show()