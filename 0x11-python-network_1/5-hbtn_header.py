#!/usr/bin/python3
'''Python script that displays the value of the variable
X-Request-Id in the response header'''
if __name__ == '___main__':
    import requests
    import sys

    url = sys.argv[1]

    response = requests.get(url)

    request_id = response.headers.get('X-Request-Id')

    # Display the value of the X-Request-Id header
    print(request_id)
