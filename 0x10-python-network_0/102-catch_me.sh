#!/bin/bash
# This is a comment explaining what this script does.
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"
