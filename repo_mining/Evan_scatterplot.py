import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import csv
from datetime import datetime

# Read the CSV file that contains the authors and commit dates for each file
def read_author_date_csv(file_path):
    data = []
    earliest_date = None
    latest_date = None
    
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            filename, author, commit_date = row
            date_obj = datetime.strptime(commit_date, "%Y-%m-%d %H:%M:%S")
            week_number = date_obj.isocalendar()[1]  # Get the ISO week number
            year = date_obj.year
            week_of_year = date_obj.strftime("%Y-%U")  # Get the year and week number in the format "YYYY-WW"
            
            # Track the earliest and latest commit dates
            if not earliest_date or date_obj < earliest_date:
                earliest_date = date_obj
            if not latest_date or date_obj > latest_date:
                latest_date = date_obj

            data.append([filename, author, commit_date, year, week_number, week_of_year])
    
    # Now we calculate the week number relative to the earliest commit
    start_date = earliest_date
    for entry in data:
        commit_date = datetime.strptime(entry[2], "%Y-%m-%d %H:%M:%S")
        # Calculate the number of weeks since the first commit
        weeks_since_start = (commit_date - start_date).days // 7
        entry.append(weeks_since_start)  # Add this as a new column (weeks_since_start)

    return data, start_date, latest_date

# Create a scatter plot with files on x-axis (numbered), weeks on y-axis, shaded by author
def create_scatter_plot(data, start_date):
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(data, columns=["Filename", "Author", "Commit Date", "Year", "Week", "WeekOfYear", "WeeksSinceStart"])

    # Create a list of unique authors for distinct colors
    authors = df['Author'].unique()
    colors = list(mcolors.TABLEAU_COLORS.values())  # Use Tableau color palette
    author_color_map = {author: colors[i % len(colors)] for i, author in enumerate(authors)}

    # Plotting
    plt.figure(figsize=(12, 6))

    # Number the files and plot the points
    file_numbers = {filename: idx*2 for idx, filename in enumerate(df['Filename'].unique())}

    # Plot each commit as a scatter point
    for filename in df['Filename'].unique():
        file_data = df[df['Filename'] == filename]
        for _, row in file_data.iterrows():
            # Plot each point with weeks since start on y-axis and file number on x-axis
            plt.scatter(file_numbers[filename], row['WeeksSinceStart'], color=author_color_map[row['Author']], alpha=0.7)

    # Set the x-axis labels (with file numbers) and remove duplicate legends
    file_labels = list(file_numbers.keys())
    plt.xticks(ticks=list(file_numbers.values()), labels=[f'{i+1}' for i in range(len(file_labels))])

    # Set labels and title
    plt.ylabel('Weeks')
    plt.xlabel('File')

    # Show grid
    plt.grid(True)

    # Display the plot
    plt.tight_layout()
    plt.show()

# Example usage
input_csv = 'data/authors_and_dates.csv'  # Path to the CSV file containing the authors and commit dates

# Read the data and create the scatter plot
data, start_date, latest_date = read_author_date_csv(input_csv)
create_scatter_plot(data, start_date)
