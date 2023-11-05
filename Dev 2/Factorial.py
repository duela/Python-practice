# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 03:43:48 2022

@author: yinku
"""

print('Please choose value')

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
elif num <= 366:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
else:
    print("Value is too high")

def factorial(n):
    if n == 0:
        return 1
    else:
        f = n * factorial(n - 1)
        return f