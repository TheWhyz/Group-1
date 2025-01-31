import numpy as np
import csv
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
from datetime import datetime

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Touches", "Date"]
df = pd.read_csv("data/file_rootbeer.csv", usecols=columns)
print("Contents in csv file: ", df)
plt.plot(df.Touches, df.Date)

##########################################################
filename = open('data/file_rootbeer.csv', 'r')
file = csv.DictReader(filename)

# creating empty lists
filename_set = set()
seen_filenames = []
all_files = []
touches = []
name = []
date = []
week = []

for row in file:  # for each row in the csv file
    # first append it to a list that contains all the filenames EVEN duplicates
    filename = row['Filename']
    all_files.append(filename)

    if filename not in filename_set:  # check if duplicate
        filename_set.add(filename)
        seen_filenames.append(filename)

    touches.append(row['Touches'])
    name.append(row['Author'])
    date.append(row['Date'])

    newdate = datetime.fromisoformat(row['Date'].replace("Z", "+00:00"))
    week_number = newdate.isocalendar()[1]
    week.append(week_number)

print('filenames:', seen_filenames)
print('All filenames:', all_files)
print('The touches:', touches)
print('The name:', name)
print('The date:', date)
print('Week', week)

###############################################################################
########################################################################################
file_indices = list(range(len(seen_filenames)))

onebyone_authors = list(set(name))
colors = list(mcolors.TABLEAU_COLORS.values())  #coloring
author_colors = {author: colors[i % len(colors)] for i, author in enumerate(onebyone_authors)}

plt.figure(figsize=(10, 5))
for i in range(len(file_indices)):
    plt.scatter(file_indices[i], week[i], marker='o', color=author_colors[name[i]], alpha=0.7)

plt.ylabel("Weeks")
plt.xlabel("Files")
plt.show()

