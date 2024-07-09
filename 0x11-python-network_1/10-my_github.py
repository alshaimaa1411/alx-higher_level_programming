#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password"""
import requests
import sys


def fetch_github_id(username, password):
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        print(data['id'])
    else:
        print("None")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    fetch_github_id(username, password)
