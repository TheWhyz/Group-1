import csv
import matplotlib.pyplot as plt
from datetime import datetime

# CSV data
data = []
authorset = set()
sdate = None # starting date variable

with open('rootbeer_authors_dates_data.csv', mode = 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        filename = row['Filename']
        author = row['Author'].strip().lower()
        date = datetime.strptime(row['Date'], '%Y-%m-%dT%H:%M:%SZ')
        authorset.add(author)

        if sdate is None:
            sdate = date
        else:
            if date < sdate:
                sdate = date

        data.append({'filename': filename, 'author': author, 'date': date})

# Generate scatter plot
def generate_scatter_plot(data, authorset, sdate, output='scatter_plot.png'):
    filenms = set()
    # loop through the data
    for entry in data:
        filenms.add(entry['filename'])

    uniquef = sorted(filenms) # unique files
    filelst = {}

    for index, file in enumerate(uniquef):
        filelst[file] = index

    cmap = plt.colormaps.get_cmap('tab20')
    colors = cmap.colors
    acolors = {}

    for author, color in zip(authorset, colors):
        acolors[author.strip()] = color

    x, y, colors = [], [], []

    for entry in data:
        fname = entry['filename']  #filename

        if fname not in filelst:
            print(f"Skipping unmapped file: {fname}")
            continue

        findex = filelst[fname] # file index
        weeks = (entry['date'] - sdate).days // 7
        akey = entry['author'].lower().strip() # author keys
        color = acolors.get(akey, 'black') # default color
        x.append(findex)
        y.append(weeks)
        colors.append(color)

    plt.figure(figsize=(9, 5))  # dimensions
    plt.scatter(x, y, c=colors, alpha=0.6, edgecolor='k')

    # Labels
    plt.xlabel('File')
    plt.ylabel('Weeks')
    plt.title('Files touched throughout the weeks by authors')
    tpos = list(filelst.values())  # for the ticks positions
    tlabels = list(range(len(filelst)))  # for the tick labels


    plt.xticks(ticks=tpos, labels=tlabels, fontsize=8)

    lst = []

    # Loop authors and colors
    for author, color in acolors.items():
        legendt = plt.Line2D([0], [0], marker='o', color=color, linestyle='', label=author)
        lst.append(legendt)

    plt.legend(handles=lst, bbox_to_anchor=(1.05, 1), loc='upper left', title="Authors")
    plt.tight_layout()

    plt.savefig(output, bbox_inches='tight')
    plt.show()

generate_scatter_plot(data, authorset, sdate)
