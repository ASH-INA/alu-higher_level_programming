#!/usr/bin/python3
"""
This script fetches url using urllib and displays the body of the response.
"""

import urllib.request

url = "https://alu-intranet.hbtn.io/status"
with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
