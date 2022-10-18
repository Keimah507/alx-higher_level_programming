#!/usr/bin/python3
"""Takes in URl, sends request to URL and displays value of variable
X-request-Id in response header"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
