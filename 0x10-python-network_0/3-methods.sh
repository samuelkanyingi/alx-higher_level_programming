#!/bin/bash
# cURL only methods
 curl -s -X OPTIONS -i "$1" | grep -i "Allow:" | cut -d' ' -f2-
