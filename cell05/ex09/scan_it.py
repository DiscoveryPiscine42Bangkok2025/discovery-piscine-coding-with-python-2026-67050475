#!/usr/bin/env python3
import sys, re

if (len(sys.argv) == 3):
    x = re.findall(sys.argv[1], sys.argv[2], re.IGNORECASE)
    if (len(x) > 0):
        print(len(x))
    else:
        print("none")
else:
    print("none")