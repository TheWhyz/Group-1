import json
import requests
import csv
import os

# Ensure output directory exists
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
        print(e)
    return jsonData, ct

# Fetch repository programming languages to dynamically determine source file types
def get_repo_languages(repo, lsttokens):
    url = f"https://api.github.com/repos/{repo}/languages"
    jsonData, _ = github_auth(url, lsttokens, 0)
    return [lang.lower() for lang in jsonData.keys()]

# Map programming languages to file extensions
language_extensions = {
    "python": [".py"],
    "java": [".java"],
    "javascript": [".js"],
    "c++": [".cpp", ".h"],
    "c": [".c", ".h"],
    "c#": [".cs"],
    "kotlin": [".kt", ".kts"],
    "ruby": [".rb"],
    "go": [".go"],
    "php": [".php"],
    "html": [".html"],
    "css": [".css"]
}

# Fetch only source files and their authors with timestamps
def collect_authors_file_touches(dictfiles, lsttokens, repo):
    ipage = 1  # Pagination for commits
    ct = 0  # Token counter

    # Get repo-specific programming languages
    repo_languages = get_repo_languages(repo, lsttokens)
    valid_extensions = [ext for lang in repo_languages if lang in language_extensions for ext in language_extensions[lang]]

    try:
        while True:
            spage = str(ipage)
            commits_url = f'https://api.github.com/repos/{repo}/commits?page={spage}&per_page=100'
            json_commits, ct = github_auth(commits_url, lsttokens, ct)

            if not json_commits:  # Stop when no more commits are found
                break

            for commit_obj in json_commits:
                sha = commit_obj['sha']
                author_name = commit_obj['commit']['author']['name']
                commit_date = commit_obj['commit']['author']['date']

                sha_url = f'https://api.github.com/repos/{repo}/commits/{sha}'
                sha_details, ct = github_auth(sha_url, lsttokens, ct)

                for file_obj in sha_details.get('files', []):
                    filename = file_obj['filename']

                    # Store only source files
                    if any(filename.endswith(ext) for ext in valid_extensions):
                        if filename not in dictfiles:
                            dictfiles[filename] = []
                        dictfiles[filename].append((author_name, commit_date))
                        print(f"Collected: {filename} - {author_name} @ {commit_date}")

            ipage += 1
    except Exception as e:
        print(f"Error fetching data: {e}")
        exit(0)

# GitHub repo
repo = 'scottyab/rootbeer'

# GitHub tokens (replace with your own)
lsttokens = [""]

dictfiles = {}
collect_authors_file_touches(dictfiles, lsttokens, repo)
print('Total source files processed:', len(dictfiles))

# Save results to CSV
output_file = f'data/authors_{repo.split("/")[1]}.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Filename", "Author", "Date"])

    for filename, touches in dictfiles.items():
        for author, date in touches:
            writer.writerow([filename, author, date])

print(f"Data saved to {output_file}")