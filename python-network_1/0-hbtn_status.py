#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status using urllib and displays the body of the response.
"""

import urllib.request

url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html = response.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html.decode('utf-8'))
