#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL"""
import requests
import sys


def fetch_url(url):
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    fetch_url(url)
