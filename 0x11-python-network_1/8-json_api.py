#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

"""
from sys import argv
import requests


if __name__ == "__main__":
    msg = "" if len(argv) == 1 else argv[1]
    p = {"q": msg}

    r = requests.post("http://0.0.0.0:5000/search_user", data=p)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
