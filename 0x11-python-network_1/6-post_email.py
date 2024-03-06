#!/usr/bin/python3
'''
Python script that displays the body of the response
'''
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})

    print(response.text)
