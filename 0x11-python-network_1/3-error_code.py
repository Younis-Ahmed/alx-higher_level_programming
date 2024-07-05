#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

from sys import argv
from urllib import request, error

if __name__ == "__main__":
    url = argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as res:
            print(res.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
