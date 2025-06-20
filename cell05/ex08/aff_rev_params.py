#!/usr/bin/env python3
import sys

argv = sys.argv[1:]
 
if len(argv) == 0:
    print("none")
else:
    for arg in reversed(argv):
        print(arg)