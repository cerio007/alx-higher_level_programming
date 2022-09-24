#!/usr/bin/python3
"""Python script that shows thw last 10 commits of a GitHub
repository.
"""
import sys
from requests import get, auth


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    res = requests.get(url)
    commit = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commit[i].get("sha"),
                commit[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
