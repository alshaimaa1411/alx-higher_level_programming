#!/usr/bin/python3
"""Python script that takes in a URL and an email address"""
import requests
import sys


def send_post_request(url, email):
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
