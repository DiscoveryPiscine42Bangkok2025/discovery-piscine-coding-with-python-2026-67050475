#!/usr/bin/env python3
import sys

def shrink(x):
    print(x[0:8])

def enlarge(x):
    while (len(x) < 8):
        x += "Z"
    print(x)

if (len(sys.argv) == 1):
    print("none")
else:
    for x in sys.argv[1:]:
        if (len(x) < 8):
            enlarge(x)
        elif (len(x) > 8):
            shrink(x)
        else:
            print(x)