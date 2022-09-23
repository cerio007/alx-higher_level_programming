#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the value of a variable in the response header
"""
import requests
import sys


if __name__ == "__main__":
    try:
        a = requests.get(sys.argv[1])
        print(a.headers['X-Request-Id'])
    except IndexError:
        pass
