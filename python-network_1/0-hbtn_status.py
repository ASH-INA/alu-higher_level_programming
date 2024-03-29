#!/usr/bin/python3
"""
This script fetches url using urllib and displays the body of the response.
"""

import urllib.request

url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html)
