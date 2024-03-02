#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id variable"""
import urllib.request
import sys

if __name__ == '__main__':
    arg = sys.argv[1]
    with urllib.request.urlopen(arg) as r:
        x_request_id = r.headers.get('X-Request-Id')
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id header not found in the response.")
