#!/usr/bin/python3
"""fetches the URL"""

if__name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- content: {}'.format(type(r.text)))
    print('\t- content: {}'.fomat(r.text))
