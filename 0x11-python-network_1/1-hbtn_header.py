#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL"""
import urllib.request
import sys


def fetch_x_request_id(url):
    try:
        # Create a request object
        req = urllib.request.Request(url)

        # Send the request and get the response
        with urllib.request.urlopen(req) as response:
            # Check if X-Request-Id header is present
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(f"{x_request_id}")
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print(f"{e}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python fetch_x_request_id.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
