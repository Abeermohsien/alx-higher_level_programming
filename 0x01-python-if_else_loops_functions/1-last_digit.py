#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
if number > 10:
    rem = number % 10
else:
    rem = number % -10
print(f"Last digit of {number:d} is {rem:d} and is ")
if rem > 5:
    print("greater then 5")
elif rem == 0:
    print("0")
else:
    print("less than 6 and not 0")
