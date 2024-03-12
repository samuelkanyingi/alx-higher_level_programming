#!/usr/bin/python3
'''Python script that takes 2 arguments in order to solve this challenge'''
if __name__ == '__main__':
    import requests
    import sys

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Define the GitHub API endpoint for retrieving commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        commits = response.json()

        # Print the list of commits
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Failed to retrieve commits. Status code:", response.status_code)
