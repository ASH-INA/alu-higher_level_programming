#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
