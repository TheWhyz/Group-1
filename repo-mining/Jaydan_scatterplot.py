import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
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
color_map = {author: cm.rainbow(i / len(authors)) for i, author in enumerate(authors)}

# Create scatter plot
plt.figure(figsize=(10, 6))

for _, row in df.iterrows():
    plt.scatter(
        [row["FileIndex"]] * len(row["Weeks"]),
        row["Weeks"],
        color=color_map[row["Author"]],
        alpha=0.7,
    )

plt.xlabel("file")
plt.ylabel("weeks")
plt.show()
