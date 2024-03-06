#!/usr/bin/python3
''' Python script that fetches url'''
if __name__ == '__main__':
    import requests
    # Send a GET request to the URL
    response = requests.get('https://alx-intranet.hbtn.io/status')


    print('Body response:')
    print('\t- type:', type(response.text))
    print('\t- content:', response.text)
