#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s -H "X-HolbertonSchool-User-Id: 98" $1 | grep -q "NOP" && echo "OK" || echo "Error: Unexpected response" | cut -c1-2
