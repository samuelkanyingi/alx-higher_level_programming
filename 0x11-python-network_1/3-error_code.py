#!/usr/bin/python3
'''print: Error code: followed by the HTTP status code'''
if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys


    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')
        print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
