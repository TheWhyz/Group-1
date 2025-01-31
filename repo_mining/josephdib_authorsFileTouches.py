import json
import requests
import csv
import os

if not os.path.exists("data"):
    os.makedirs("data")

# GitHub Authentication function
def github_auth(url, lsttokens, ct):
    jsonData = None
    try:
        ct = ct % len(lsttokens)
        headers = {'Authorization': 'Bearer {}'.format(lsttokens[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        pass
        print(e)
    return jsonData, ct

# @dictfiles, empty dictionary of files
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter

    #File extentions to grab from
    file_exts = ['.py', '.java', '.js', '.cpp', '.c', '.cs', '.kts', '.kt', '.rb', '.go', '.php', '.html', '.css']

    try:
        # loop through all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = f'https://api.github.com/repos/{repo}/commits?page={spage}&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            # break out of the while loop if there are no more commits in the pages
            if not jsonCommits:
                break
            # iterate through the list of commits in spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                author = shaObject['commit']['author']['name']
                date = shaObject['commit']['author']['date']

                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                
                # gets the info of the file if it is a source file
                if 'files' in shaDetails:
                    for filenameObj in shaDetails['files']:
                        filename = filenameObj['filename']
                        if any(filename.endswith(ext) for ext in file_exts):
                            if filename not in dictfiles:
                                dictfiles[filename] = []
                            dictfiles[filename].append((author, date))
                            print(filename, author, date)
            ipage += 1
    except:
        print("Error receiving data:")
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
lstTokens = [""]

dictfiles = dict()
countfiles(dictfiles, lstTokens, repo)
print('Total number of files: ' + str(len(dictfiles)))

file = repo.split('/')[1]
fileOutput = 'data/file_' + file + '.csv'

with open(fileOutput, 'w', newline='') as fileCSV:
    writer = csv.writer(fileCSV)
    writer.writerow(["Filename", "Touches", "Author", "Timestamp"])
    
    bigcount = 0
    bigfilename = None
    
    for filename, touches in dictfiles.items():
        for author, timestamp in touches:
            writer.writerow([filename, len(touches), author, timestamp])
        if len(touches) > bigcount:
            bigcount = len(touches)
            bigfilename = filename

fileCSV.close()
print('The file ' + bigfilename + ' has been touched ' + str(bigcount) + ' times.')
