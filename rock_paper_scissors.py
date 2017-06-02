#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:05:15 2016

@author: NABRARPOUR4
"""
"""
The program should do the following:

1 - Prompt the user to select either Rock, Paper, or Scissors
2 - Instruct the computer to randomly select either Rock, Paper, or Scissors
3 - Compare the user's choice and the computer's choice
4 - Determine a winner (the user or the computer)
5 - Inform the user who the winner is
"""

from random import randint ###randint is not a built_in function
from time import sleep

options = ["R", "P", "S"]
lost_msg = "VOCE PERDEU, TENTE OUTRA VEZ."
won_msg = "PARABENS, VOCE GANHOU. MESTRE."

def decide_winner(user_choice, computer_choice):
    print "You selected: %s" % user_choice
    print "Computer selecting..."
    sleep(1)
    print "The Computer selected: %s" % computer_choice
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print "It's a tie."
    elif user_choice_index == 0 and computer_choice_index == 2:
        print won_msg
    elif user_choice_index == 1 and computer_choice_index == 0:
        print won_msg
    elif user_choice_index == 2 and computer_choice_index == 1:
        print won_msg
    elif user_choice_index > 2 or computer_choice_index > 2:
        print "Invalid option selected"
        return
    else:
        print lost_msg
        
""" The above function decides who the winner is between the user and 
the computer, but we haven't written a function that actually starts the game.
 Let's do that now."""

def play_RPS():
    print "Rock, Paper, or Scissors?"
    user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors:")
    sleep(1)
    user_choice = user_choice.upper()   #To be Consistent with the format of our list
    computer_choice = options[randint(0,len(options)-1)]  #Step 25 - This is a more dynamic line of code that will adapt to the size of the options list if it ever grows.
    decide_winner(user_choice,computer_choice) ## The user has now submitted their choice and the computer has also made a random choice. It's time to determine a winner. 

play_RPS()

"""'Let's approach this problem with a glass half full mentality: we'll print 
only the scenarios in which the user wins, otherwise the user will have lost.

What are the scenarios in which the user wins?

User: Rock, Computer: Scissors
User: Paper, Computer: Rock
User: Scissors, Computer: Paper
"""

""" Step 25 - Create a variable called computer_choice. As in the last step, set it 
equal to a random element of the options list using randint. However,
instead of using 0 and 2 in the randint function, use 0 as the first integer,
and use len(options)-1 as the second integer. This will ensure that if
 we ever add more options to the game, we won't have to change this line 
 of code. (Of course, there might be more rules.)"""


