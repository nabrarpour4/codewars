#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:09:29 2016

@author: NABRARPOUR4
"""

""" Wanna play a game? In this project, we'll build a program that rolls
 a pair of dice and asks the user to guess a number. Based on the user's 
 guess, the program should determine a winner. If the user's guess is greater 
 than the total value of the dice roll, they win! Otherwise, the computer wins.
    1.) Randomly roll a pair of dice
    2.) Add the values of the roll
    3.) Ask the user to guess a number
    4.) Compare the user's guess to the total value
    5.) Decide a winner (the user or the program)
    6.) Inform user who is the final winner
"""
import math
from random import randint
from time import sleep

"""Begin by creating a function that prompts user for their guess. """ 

def get_user_guess(): 
    user_guess = int(raw_input("Guess a number: "))  
    #raw_input by default stores answer in a string, so we need to wrap the int()
    return user_guess      #returns user's guess on the next line

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2 
    print "The maximum value possible is " + str(max_val)
    sleep(1)
    user_guess = get_user_guess()    #Store the returned value into a variable called user_guess
    if user_guess > max_val:    # checks if the user's guess is greater than the maximum value
        print "No guessing higher than maximum possible value!"
        return
    else: 
        print "Rolling...."
        sleep(2)
        print "The first value is: %d" % first_roll
        sleep(1)
        print "The first value is: %d" % second_roll
        sleep(1)
        total_roll = sum([first_roll, second_roll])
        print "The Total roll is: %d" % total_roll
        print "Result..."
        sleep(1)
        if user_guess > total_roll: 
            print "You won! \n Computer loses"
            return
        else: 
            print "You lost, and have been defeated by the PC"
            return 
        
roll_dice(6)