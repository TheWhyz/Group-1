import json
import requests
import csv

import os

if not os.path.exists("data"):
 os.makedirs("data")

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
        pass
        print(e)
    return jsonData, ct



# @dictFiles, empty dictionary of files
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter
    # Add a list of source file extensions
    source_file_extensions = ['.py', '.java', '.js', '.cpp', '.c', '.cs', '.kts', '.kt', '.rb', '.go', '.php', '.html', '.css']
    try:
        # loop though all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            # break out of the while loop if there are no more commits in the pages
            if len(jsonCommits) == 0:
                break
            # iterate through the list of commits in  spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                filesjson = shaDetails['files']
                author = shaDetails["commit"]["author"]["name"]
                date = shaDetails["commit"]["author"]["date"]
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    # Check if the file has a source file extension
                    if any(filename.endswith(ext) for ext in source_file_extensions):
                        if filename not in dictfiles:
                            dictfiles[filename] = {}
                        if author not in dictfiles[filename]:
                            dictfiles[filename][author] = {'dates': [], 'count': 0}
                        dictfiles[filename][author]['dates'].append(date)
                        dictfiles[filename][author]['count'] += 1
                        print(f"{filename} touched by {author} on {date}")
            ipage += 1
    except:
        print("Error receiving data")
        exit(0)
# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = []

dictfiles = dict()
countfiles(dictfiles, lstTokens, repo)
print('Total number of files: ' + str(len(dictfiles)))

file = repo.split('/')[1]
# change this to the path of your file
fileOutput = 'data/authorsTouched.csv'
rows = ["Filename", "Author", "Date", "Touches"]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)

for filename, authors in dictfiles.items():
    for author, details in authors.items():
        dates = "; ".join(details['dates'])
        rows = [filename, author, dates, details['count']]
        writer.writerow(rows)

fileCSV.close()
print("CSV file created with authors, dates, and touch counts.")
