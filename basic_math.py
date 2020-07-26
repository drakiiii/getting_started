#!/usr/bin/env python3.8

for x,y in range(0,100):
    y = (x ** 2) - 1
    if y == x:
        print(x,y)
    else:
        print("No pair matches this requirement.")