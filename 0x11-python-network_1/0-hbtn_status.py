#!/usr/bin/python3
"""urlib"""
from urllib.request import urlopen
url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as response:
    body = response.read()