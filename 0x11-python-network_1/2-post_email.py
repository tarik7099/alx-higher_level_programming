#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed URL
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
