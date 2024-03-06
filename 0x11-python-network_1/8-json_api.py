#!/usr/bin/python3
''' Python script that display the id and name JSON format'''
if __name__ = '__main__':
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
