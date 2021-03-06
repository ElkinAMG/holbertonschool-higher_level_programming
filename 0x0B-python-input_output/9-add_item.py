#!/usr/bin/python3
'''

This module contains `imports`.

'''
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    obj = load_from_json_file("add_item.json")
except:
    obj = []
for i in range(1, len(argv)):
    obj.append(argv[i])
save_to_json_file(obj, "add_item.json")
