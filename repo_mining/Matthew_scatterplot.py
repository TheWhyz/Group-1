import matplotlib.pyplot as plt
import random
from datetime import datetime
import json

# load date
def load_file_touches(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

# get first date
def get_earliest_date(file_touches):
    earliest_date = None
    for touches in file_touches.values():
        for _, date in touches:
            current_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
            if earliest_date is None or current_date < earliest_date:
                earliest_date = current_date
    return earliest_date

# calculate weeks
def calculate_weeks(start_date, date_str):
    current_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ") 
    delta = current_date - start_date
    return delta.days // 7

# scatter plot part
def generate_scatter_plot(file_touches, start_date):
    authors = list({author for touches in file_touches.values() for author, _ in touches})
    colors = {author: (random.random(), random.random(), random.random()) for author in authors}

    plt.figure(figsize=(14, 10))  
    for file_idx, (file, touches) in enumerate(file_touches.items()):
        for author, date in touches:
            weeks = calculate_weeks(start_date, date)
            plt.scatter(file_idx, weeks, color=colors[author], label=author, s=50, alpha=0.8)

    # labels and titles
    plt.xlabel("File Index", fontsize=14)
    plt.ylabel("Weeks Since Project Start", fontsize=14)
    plt.title("File Touches Over Time by Authors", fontsize=16)

    # prevent dupes
    handles, labels = plt.gca().get_legend_handles_labels()
    unique_labels = {label: handle for handle, label in zip(handles, labels)}
    plt.legend(unique_labels.values(), unique_labels.keys(), title="Authors", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data_filepath = "file_touches.json" 

    # load data file
    file_touches = load_file_touches(data_filepath)

    # find start date
    earliest_date = get_earliest_date(file_touches)
    print(f"Earliest commit date (project start): {earliest_date}")

    # make graph
    generate_scatter_plot(file_touches, earliest_date)
