#!/usr/bin/python3
"""
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    letter = ""  if len(sys.argv) == 1 else sys.argv[1]
    pay_load = {"q": letter}

    url = requests.post('http://0.0.0.0:5000/search_user', data=pay_load)

    try:
        json_a = url.json()
        if not json_a:
            print("No result")
        else:
            print("[{}] {}".format(json_a.get('id'), json_a.get('name')))
    except ValueError:
        print("Not a valid JSON")
