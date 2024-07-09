#!/usr/bin/python3
"""Python script that takes in a URL and an email"""
import urllib.parse
import urllib.request
import sys

def send_post_request(url, email):
    # Encode the email as a URL parameter
    params = urllib.parse.urlencode({'email': email})
    params = params.encode('utf-8')  # Encode the parameters to bytes

    # Make a POST request
    with urllib.request.urlopen(url, data=params) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
