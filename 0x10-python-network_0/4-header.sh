#!/bin/bash
#takes in a URL as an argument, sends GET request and displays body
curl -s "$1" -X GET -H "X-School-User_id:98"
