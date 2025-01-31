import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

df = pd.read_csv("data/authorsTouched.csv")

# Convert 'Date' to list of datetime objects
df["Date"] = df["Date"].apply(
    lambda x: [datetime.strptime(d, "%Y-%m-%dT%H:%M:%SZ") for d in x.split("; ")]
)

# Flatten all dates to find the earliest date
all_dates = [date for sublist in df["Date"] for date in sublist]
min_date = min(all_dates)

# Convert dates to weeks since the earliest date
df["Weeks"] = df["Date"].apply(lambda dates: [(d - min_date).days // 7 for d in dates])

# Assign numeric values to filenames for plotting
file_map = {file: idx for idx, file in enumerate(df["Filename"].unique())}
df["FileIndex"] = df["Filename"].map(file_map)

# Assign colors based on authors
authors = df["Author"].unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(authors)))
color_map = dict(zip(authors, colors))

# Create scatter plot
plt.figure(figsize=(10, 6))

for author in authors:
    author_data = df[df["Author"] == author]
    for _, row in author_data.iterrows():
        plt.scatter(
            [row["FileIndex"]] * len(row["Weeks"]),
            row["Weeks"],
            color=color_map[author],
            alpha=0.7,
            label=author if author not in plt.gca().get_legend_handles_labels()[1] else ""
        )

plt.xlabel("File")
plt.ylabel("Weeks")
plt.legend(title="Authors", bbox_to_anchor=(1.05, 1), loc='center left')
plt.tight_layout()
plt.show()
