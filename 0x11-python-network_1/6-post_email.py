#!/usr/bin/python3
"""Takes in URL and email address, sends POST request to passed URL with email
as parameter, and passes body of the response"""


if __name__ == "__main__"
import requests
import sys

r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(r.text)
