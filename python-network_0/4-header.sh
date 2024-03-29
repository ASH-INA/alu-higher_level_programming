#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL, and displays the body of the response
response=$(curl -s -H "X-HolbertonSchool-User-Id: 98" $1)
if [ "$response" = "NOP" ]; then
    echo "OK"
else
    echo "Error: Unexpected response"
    exit 1
fi
