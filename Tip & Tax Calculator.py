#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 19:42:30 2016

@author: NABRARPOUR4
"""

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

""" With tax: 108.0000 
    With tip: 124.0000
    None                 """


def hello_world():
    print "Hello World"

""" The header of a function = def function_name(parameters_of_function) 
        function_body = describes the procedures for execution """
        
