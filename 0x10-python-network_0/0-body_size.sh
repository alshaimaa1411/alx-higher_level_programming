#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Send a GET request to the URL and capture the response body size
response=$(curl -sI "$url" | grep -i 'content-length' | awk '{print $2}')

# Check if response contains Content-Length header
if [ -z "$response" ]; then
    echo "Error: Content-Length header not found in the response."
    exit 1
fi

echo "$response"
