#!/usr/bin/python3
"""fetches the URL"""

if __name__ == "__main__" :
    import requests

    r = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- content: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
