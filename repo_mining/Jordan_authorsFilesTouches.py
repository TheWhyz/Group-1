import json
import requests
import csv
import os

if not os.path.exists("data"):
    os.makedirs("data")

# GitHub Authentication function
def github_auth(url, lsttokens, ct):
    json_data = None
    try:
        ct = ct % len(lsttokens)
        headers = {'Authorization': 'Bearer {}'.format(lsttokens[ct])}
        request = requests.get(url, headers=headers)
        json_data = json.loads(request.content)
        ct += 1
    except Exception as e:
        print(e)
    return json_data, ct

# Collects commit details including authors and timestamps
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # URL page counter
    ct = 0  # Token counter

    try:
        # Loop through all commit pages until the last empty page
        while True:
            spage = str(ipage)
            commits_url = f'https://api.github.com/repos/{repo}/commits?page={spage}&per_page=100'
            json_commits, ct = github_auth(commits_url, lsttokens, ct)

            # Break if there are no more commits
            if len(json_commits) == 0:
                break

            # Iterate through commits
            for sha_object in json_commits:
                sha = sha_object['sha']
                author_name = sha_object['commit']['author']['name']
                commit_date = sha_object['commit']['author']['date']

                # Fetch file modifications for each commit
                sha_url = f'https://api.github.com/repos/{repo}/commits/{sha}'
                sha_details, ct = github_auth(sha_url, lsttokens, ct)

                files_json = sha_details.get('files', [])
                for filename_obj in files_json:
                    filename = filename_obj['filename']

                    if filename not in dictfiles:
                        dictfiles[filename] = {'count': 0, 'authors': []}

                    dictfiles[filename]['count'] += 1
                    dictfiles[filename]['authors'].append((author_name, commit_date))

                    print(f"{filename} - {author_name} on {commit_date}")

            ipage += 1
    except Exception as e:
        print("Error receiving data:", e)
        exit(0)

# GitHub repository
repo = 'scottyab/rootbeer'

# GitHub tokens (Replace with your own valid tokens)
lstTokens = ["",
             "",
             ""]

dictfiles = dict()
countfiles(dictfiles, lstTokens, repo)
print(f'Total number of files: {len(dictfiles)}')

# Output file path
file = repo.split('/')[1]
file_output = f'data/file_{file}.csv'

# Write data to CSV file
with open(file_output, 'w', newline='') as file_csv:
    writer = csv.writer(file_csv)
    writer.writerow(["Filename", "Touches", "Authors & Dates"])

    bigcount = 0
    bigfilename = ""

    for filename, data in dictfiles.items():
        author_dates = "; ".join([f"{auth} ({date})" for auth, date in data['authors']])
        writer.writerow([filename, data['count'], author_dates])

        if data['count'] > bigcount:
            bigcount = data['count']
            bigfilename = filename

print(f'The file "{bigfilename}" has been touched {bigcount} times.')