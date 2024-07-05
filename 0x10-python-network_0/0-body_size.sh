#!/bin/bash
# script that takes in a URL, sends a request to that URL, counts in byte
size=$(curl -s "$1" | wc -c); echo "$size"
