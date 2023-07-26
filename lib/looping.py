#!/usr/bin/env python3

def happy_new_year():
    i = 11
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    new_nums = list()
    for num in int_list:
        new_num = num * num
        new_nums.append(new_num)
    return new_nums

def fizzbuzz():
    i = 1
    while i < 101:
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1