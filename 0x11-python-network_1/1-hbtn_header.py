#!/usr/bin/python3
"""Takes a request of a URL, sends request to URL and displays value of
X-Request-id variable"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
