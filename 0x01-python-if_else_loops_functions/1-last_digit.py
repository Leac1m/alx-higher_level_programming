#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = ((number * -1) % 10) * -1
if last < 6:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif last == 0:
    print(f"Last digit of {number} is 0 and is 0")
else:
    print(f"Last digit of {number} is {last} and is greater than 5")