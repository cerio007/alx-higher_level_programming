#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name, repository_name)
    res = get(url)
    json_a = res.json()
    for i in range(0, 10):
        print("{}: {}".format(json_a[i].get('sha'), json_a[i].get('commit')
                              .get('author').get('name')))
