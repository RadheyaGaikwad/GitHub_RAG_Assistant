import requests

# This function fetches files from GitHub repo
def get_repo_files(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    response = requests.get(url)

    files = response.json()
    contents = []

    for file in files:
        # We only read text/code files
        if file["type"] == "file":
            file_data = requests.get(file["download_url"]).text
            
            contents.append({
                "name": file["name"],
                "content": file_data
            })

    return contents