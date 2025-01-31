import json
import requests
import csv
import os

# Ensure the data directory exists
if not os.path.exists("data"):
    os.makedirs("data")

# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lsttoken)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        print(e)
    return jsonData, ct

# Dictionary to store file details
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # URL page counter
    ct = 0  # Token counter

    try:
        while True:
            spage = str(ipage)
            commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            if len(jsonCommits) == 0:
                break

            for shaObject in jsonCommits:
                sha = shaObject['sha']
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)

                for filenameObj in shaDetails['files']:
                    filename = filenameObj['filename']
                    if filename.endswith(('.java', '.kt', '.kts', '.cpp', '.h', '.c', '.cmake')):
                        author = shaDetails['commit']['author']['name']
                        date = shaDetails['commit']['author']['date']
                        if filename not in dictfiles:
                            dictfiles[filename] = []
                        dictfiles[filename].append({'author': author, 'date': date})
                        print(filename)
            ipage += 1
    except Exception as e:
        print("Error receiving data:", e)

# GitHub repo and authentication tokens
repo = 'scottyab/rootbeer'
lstTokens = []
dictfiles = {}
countfiles(dictfiles, lstTokens, repo)
print('Total number of unique files:', len(dictfiles))

file = repo.split('/')[1]
fileOutput = file + '_authors_dates_data.csv'  # Changed to save in the current directory

with open(fileOutput, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Filename', 'Author', 'Date'])
    for filename, details in dictfiles.items():
        for detail in details:
            writer.writerow([filename, detail['author'], detail['date']])

print('data in CSV file has been written to', fileOutput)