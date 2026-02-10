#!/usr/bin/env python3

og = [2, 8, 9, 48, 8, 22,-12, 2]
new = set()
for x in og:
    if x > 5:
        new.add(x + 2)
print("Original array:", og)
print("New array:", new)