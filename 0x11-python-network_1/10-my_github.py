#!/usr/bin/python3
'''
Python script that takes your GitHub credentials
and uses the GitHub API to display your id
'''
if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_id = response.json()['id']
        print("Your GitHub user ID is:", user_id)
    else:
        print("Failed to retrieve user information. Status code:", response.status_code)
