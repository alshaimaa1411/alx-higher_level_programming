#!/usr/bin/python3
""" Python script that takes in a URL, sends a request """
import requests
import sys


def fetch_request_id(url):
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    fetch_request_id(url)
