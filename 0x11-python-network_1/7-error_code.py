#!/usr/bin/python3
"""Takes in URL, sends request to passed URL
and displays body of the response"""


import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(res.text)
