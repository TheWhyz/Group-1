import csv
import requests
import json
import os
from datetime import datetime

# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lstTokens)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        print(e)
    return jsonData, ct

# Get commit details for each file (author and date)
def get_author_and_date_for_file(repo, lsttokens, filename):
    ipage = 1  # URL page counter
    ct = 0  # token counter
    authors_and_dates = []

    try:
        while True:
            spage = str(ipage)
            commitsUrl = f'https://api.github.com/repos/{repo}/commits?path={filename}&page={spage}&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            if len(jsonCommits) == 0:
                break
            
            for commit in jsonCommits:
                author = commit['commit']['author']['name']
                date = commit['commit']['author']['date']
                date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
                authors_and_dates.append((author, date))

            ipage += 1
    except Exception as e:
        print(f"Error fetching data for {filename}: {e}")
    
    return authors_and_dates

# Main function to collect authors and dates for files from the CSV
def collect_authors_and_dates(input_csv, repo, lsttokens):
    # Reading the list of files from the CSV generated by CollectFiles.py
    files = []
    with open(input_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            files.append(row[0])

    # Collect authors and commit dates for each file
    file_author_date_data = {}
    for filename in files:
        if filename.endswith(('.py', '.java', '.js', '.cpp', '.c', '.h', '.go', '.ts', '.kt')):  # You can add more file extensions here
            print(f"Processing file: {filename}")
            author_date_info = get_author_and_date_for_file(repo, lsttokens, filename)
            file_author_date_data[filename] = author_date_info

    # Output the results to a CSV
    output_file = 'data/authors_and_dates.csv'
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Filename", "Author", "Commit Date"])
        for filename, author_date_info in file_author_date_data.items():
            for author, date in author_date_info:
                writer.writerow([filename, author, date])

    print(f"Data has been written to {output_file}")

# Example usage
repo = 'scottyab/rootbeer'  # Replace with the desired repo
lstTokens = []  # Add more tokens if necessary
input_csv = 'data/file_rootbeer.csv'  # The CSV file generated by CollectFiles.py (adjust path as needed)

collect_authors_and_dates(input_csv, repo, lstTokens)
