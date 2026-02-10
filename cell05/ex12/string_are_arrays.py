#!/usr/bin/env python3
import sys, re

if (len(sys.argv) == 2):
    x = re.findall("z", sys.argv[1])
    if (len(x) > 0):
        for y in x:
            print(y, end = "")
        print()
    else:
        print("none")
else:
    print("none")