#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL"""
import urllib.request
import urllib.error
import sys


def fetch_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    fetch_url(url)
