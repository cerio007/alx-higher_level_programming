#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""
import requests
import sys


if __name__ == "__main__":
    try:
        repository_name = sys.argv[1]
        owner_name = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name, repository_name)
        x = get(url)
        json_a = x.json()
        for i in range(0, 10):
            print("{}: {}".format(json_a[i].get('sha'), json_a[i].get('commit')
                                  .get('author').get('name')))
    except:
        pass
