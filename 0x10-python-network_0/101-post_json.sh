#!/bin/bash
'''Bash script that displays the body of the response'''
curl -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1" | jq '.'
