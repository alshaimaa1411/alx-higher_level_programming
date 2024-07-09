#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST"""
import requests
import sys


def search_user(q):
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:  # Check if JSON data is not empty
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    search_user(q)
