# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 03:10:15 2022

@author: yinku
"""
def test_add(x, y):
    return x + y
def test_subtract(x, y):
    return x - y
def test_multiply(x, y):
    return x * y
def test_divide(x, y):
    return x / y
print('Please choose operand')
print('1.Addition','2.subtraction','3.multiplication','4.division')
while True:    
    value = input('Enter operand choice 1,2,3 or 4 ')
    if value in ("1","2","3","4"):                     
        a = float(input("Input 1st number: "))
        b = float(input("Input 2nd number: "))

        if value == '1':
            print(a, "+", b, "=", test_add(a, b))

        elif value == '2':
            print(a, "-", b, "=", test_subtract(a, b))

        elif value == '3':
            print(a, "*", b, "=", test_multiply(a, b))

        elif value == '4':
            print(a, "/", b, "=", test_divide(a, b))
        j = input('Do you want to contine (Y/N)?: ')
        if j == 'Y': continue
        else:
          break
    else:
        print("Invalid Input select between 1 and 4")