#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:20:52 2016

@author: NABRARPOUR4
"""

""" Pig Latin is a language game, where you move the first letter 
of the word to the end and add "ay." So "Python" becomes "ythonpay." Here are 
the steps to generating the code

1.) Ask the user to input a word in English.
2.) Make sure the user entered a valid word.
3.) Convert the word from English to Pig Latin.
4.) Display the translation result.               """ 

print "Pig Latin"
print 'Welcome to the Pig Latin Translator!'

original = raw_input("Enter a word:")

""" string.isalpha(): checks if there alphanumeric characters in the string"""

if len(original) > 0 and original.isalpha():
    print new_word
else:
    print "empty"

pyg = 'ay'
word = original.lower()
first = original[0]

new_word = word[1:] + first + pyg
