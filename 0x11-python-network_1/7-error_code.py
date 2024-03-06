#!/usr/bin/python3
'''
Python script that print: Error code:
followed by the value of the HTTP status code
'''

if __name__ == '__main__':
    import requests
    import sys


    url = sys.argv[1]


    response = requests.get(url)


    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
