#!/bin/bash
# This is a comment explaining what this script does.
curl -so /dev/null "$1" -w "%{size_download}"
