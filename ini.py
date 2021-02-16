#!/usr/bin/python3
import sys
import os.path

if len(sys.argv) != 3:
    print("needs two arguments")
    exit(1)

# if these are files read them in
if os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]):
    set1 = set(open(sys.argv[1]).read().splitlines())
    set2 = set(open(sys.argv[2]).read().splitlines())
else:
    set1 = set(sys.argv[1].split())
    set2 = set(sys.argv[2].split())

for i in (set1 - set2):
    print(i)
