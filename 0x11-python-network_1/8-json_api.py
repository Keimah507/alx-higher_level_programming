#!/usr/bin/python3
"""takes in a letter and sends POST request to URL with letter as parameter"""


if __name__ == "__main__"
import requests
import sys

q = sys.argv[1] if len(sys.argv) > 1 else ""
r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
try:
    dict = r.json()
    if dic == {}:
        print('No result')
    else:
        print("[{}] {}".format(dict.get('id'), dict.get('name')))
except ValueError:
    print('Not a valid JSON')
