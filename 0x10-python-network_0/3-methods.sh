#!/bin/bash
# display all http
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
