import json
import requests
from collections import defaultdict

SOURCE_FILE_EXTENSIONS = [".py", ".java", ".cpp", ".js", ".ts", ".go", ".c"]

def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lsttoken)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        print(f"Requesting: {url}")  # debug
        request = requests.get(url, headers=headers, timeout=10)
        
        if request.status_code == 403:
            print("api limit")
            import time
            time.sleep(60)
            return github_auth(url, lsttoken, ct)
        
        request.raise_for_status()
        jsonData = request.json()
        ct += 1
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return jsonData, ct

def is_source_file(file_path):
    return any(file_path.endswith(ext) for ext in SOURCE_FILE_EXTENSIONS)

def collect_authors_and_dates(repo, lsttokens):
    ipage = 1
    ct = 0
    file_touches = defaultdict(list)

    try:
        while True:
            spage = str(ipage)
            commitsUrl = f'https://api.github.com/repos/{repo}/commits?page={spage}&per_page=100'
            print(f"Fetching commits from: {commitsUrl}")  # debug
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            if not jsonCommits or len(jsonCommits) == 0:
                print("No more commits to process.")
                break

            for shaObject in jsonCommits:
                sha = shaObject['sha']
                shaUrl = f'https://api.github.com/repos/{repo}/commits/{sha}'
                print(f"Fetching details for commit: {sha}")  # debug
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)

                if not shaDetails or 'commit' not in shaDetails:
                    print(f"Invalid commit details for SHA {sha}")
                    continue

                author = shaDetails['commit']['author'].get('name', 'Unknown Author')
                date = shaDetails['commit']['author'].get('date', 'Unknown Date')


                # debug part
                print(f"Commit by {author} on {date}")  

                filesjson = shaDetails.get('files', [])
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    if is_source_file(filename):
                        print(f"File touched: {filename}")  
                        file_touches[filename].append((author, date))
            ipage += 1
    except Exception as e:
        print("Error receiving data:", e)

    return file_touches

def save_file_touches(data, output_filepath):
    try:
        with open(output_filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {output_filepath}")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    repo = 'scottyab/rootbeer'
    lstTokens = ["sample"] 
    output_filepath = "file_touches.json" 

    file_touches = collect_authors_and_dates(repo, lstTokens)
    
    if file_touches:
        save_file_touches(file_touches, output_filepath)
    else:
        print("No data collected.")
