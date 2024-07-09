#!/usr/bin/python3
""" Python script that takes 2 arguments in order to solve this challenge."""
import requests
import sys


def fetch_commits(repository, owner):
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    params = {'per_page': 10}
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error fetching commits: {response.status_code}")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository> <owner>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    fetch_commits(repository, owner)
