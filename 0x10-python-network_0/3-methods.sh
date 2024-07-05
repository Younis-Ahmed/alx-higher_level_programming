#!/bin/bash
# display HTTP methods 'ALLOW'
curl -sI "$1" | awk '/Allow/ {print substr($0, index($0, $2))}'
