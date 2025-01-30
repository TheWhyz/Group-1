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
        ct = ct % len(lsttoken)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        print(e)
    return jsonData, ct

# @dictFiles, empty dictionary of files
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter
    authors_data = {}  # Initialize authors_data

    try:
        # loop though all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = f'https://api.github.com/repos/{repo}/commits?page={spage}&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            # break out of the while loop if there are no more commits in the pages
            if not jsonCommits:
                break
            # iterate through the list of commits in  spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                author = shaObject['commit']['author']['name']
                date = shaObject['commit']['author']['date']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = f'https://api.github.com/repos/{repo}/commits/{sha}'
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)

                filesjson = shaDetails.get('files', [])
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    dictfiles[filename] = dictfiles.get(filename, 0) + 1
                    print(filename)

                    if filename not in authors_data:
                        authors_data[filename] = []
                    authors_data[filename].append((author, date))

            ipage += 1
    except Exception as e:
        print(f"Error receiving data: {e}")
        exit(1)

    return authors_data  # Ensure the function returns the data

# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = ["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"]

dictfiles = {}
authors_data = countfiles(dictfiles, lstTokens, repo)  # Capture returned data

print(f'Total number of files: {len(dictfiles)}')

file = repo.split('/')[1]
# change this to the path of your file
fileOutput = f'data/authors_file_{file}.csv'

with open(fileOutput, 'w', newline='') as fileCSV:
    writer = csv.writer(fileCSV)
    writer.writerow(["Filename", "Touches", "Authors and Dates"])

    bigcount = None
    bigfilename = None
    for filename, count in dictfiles.items():
        writer.writerow([filename, count, json.dumps(authors_data.get(filename, []))])
        if bigcount is None or count > bigcount:
            bigcount = count
            bigfilename = filename

print(f'The file {bigfilename} has been touched {bigcount} times.')
