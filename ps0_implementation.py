# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 14:03:22 2026

@author: ioseth
"""
import sys
import numpy


def main():
    print('ps0.py program start')

    
    number1 = float(input("enter number for x:"))
    number2 = float(input("enter number for y:"))
  

#     validInput = 0;
#     if type(number1) == int:
#         validInput +=1;
#     elif type(number1) == float:
#         validInput +=1;
#     if type(number2) == int:
#         validInput +=1;
#     elif type(number2) == float:    
#         validInput +=1;
#         
#     if validInput != 2:
#         print('invalid inputs , enter only float or integers ')
#         sys.exit() 
    
    result1= numpy.power(number1,number2)
    result2= numpy.log2(number1)
    
    print("x eleveted to y aka x**y:",result1)
    print("logarith base2 of x:", result2)

if __name__ == '__main__':
    main()