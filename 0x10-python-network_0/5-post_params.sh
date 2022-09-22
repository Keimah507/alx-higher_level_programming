#!/bin/bash
#takes in a URL, sends a POST request and displays body of response
curl -s "$1" -X POST -d 'email=test.gmail.com' -d 'subject=I will always be here for pld'
