#!/bin/bash
# This is a comment explaining what this script does.
curl -sX POST -H "Content-Type: application/json" -d "$(cat $2)" "$1"
