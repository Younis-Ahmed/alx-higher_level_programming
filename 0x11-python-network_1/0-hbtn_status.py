#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as res:
        res = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode(encoding='utf-8')))
