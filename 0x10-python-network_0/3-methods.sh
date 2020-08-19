#!/bin/bash
# This is a comment explaining what this script does.
curl -sI "$1" | grep "Allow: " | cut -d" " -f 2-
