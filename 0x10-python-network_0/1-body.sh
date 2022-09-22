#!/bin/bash
#takes in URL, sends a GET request, displays body of response
curl -sI "$1" -X GET -L
