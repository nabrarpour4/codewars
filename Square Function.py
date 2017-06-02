#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:47:40 2016

@author: NABRARPOUR4
"""

def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

print square(10)  # Prints "10 squared is 100."


""" A function can require as many parameters as you'd like, but when you call 
the function, you should generally pass in a matching number of arguments. """ 


def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(2, 5)  # Add your arguments here!
