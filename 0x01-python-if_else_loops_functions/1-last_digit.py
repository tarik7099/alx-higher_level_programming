#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number1 = number % -10
elif number >= 0:
    number1 = number % 10
Last = "Last digit of"
if number1 > 5:
    print(f"{Last} {number} is {number1} and is greater than 5")
elif number1 == 0:
    print(f"{Last} {number} is {number1} and is 0")
elif number1 < 6:
    print(f"{Last} {number} is {number1} and is less than 6 and not 0")
