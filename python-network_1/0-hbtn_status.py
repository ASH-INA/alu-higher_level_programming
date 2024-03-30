#!/usr/bin/python3
"""
This script fetches url using urllib and displays the body of the response.
"""

import urllib.request

url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()  # Read the response body as bytes
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf-8'))
