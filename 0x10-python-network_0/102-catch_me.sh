#!/bin/bash
'''Send a POST request with the specified data to the URL'''
curl -s -X PUT --data "user_id=98" "0.0.0.0:5000/catch_me" -d "You got me!"
