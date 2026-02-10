#!/usr/bin/env python3
import sys

if (len(sys.argv) == 3):
    x = [y for y in range(int(sys.argv[1]), int(sys.argv[2]) + 1)]
    print(x)
else:
    print("none")