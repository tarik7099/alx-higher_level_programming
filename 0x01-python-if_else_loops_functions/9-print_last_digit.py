#!/usr/bin/python3
def print_last_digit(number):
    last_dt = (number % 10) if number >= 0 else ((number * -1) % 10)
    print(last_dt, end='')
    return (last_dt)
