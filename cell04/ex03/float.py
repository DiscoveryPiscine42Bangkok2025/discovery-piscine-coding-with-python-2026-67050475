#!/usr/bin/env python3

x = float(input("Give me a number: "))
y = int(x)
z = x - y
if (z == 0):
    print("This number is an integer.")
else:
    print("This number is a decimal.")