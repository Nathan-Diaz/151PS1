#====================================================
# Filename: Prob2.py
# 
# Your name: Nathan G. Diaz
# Who did you work with (if anyone)?:
# Estimate for time spent (in hrs)?: 7
#====================================================

import karel

# Your program should create a checkerboard pattern on any
# rectangular world. I am defining a few functions below to
# get you started, but you can (and should) add whatever
# other helper functions you want below.

def create_checkerboard():
    """ Main function to create the checkerboard pattern. Places beeper first in order to match assignment photo;
    if 'street' runs, if fron is clear then the rest of 'city' runs. """
    put_beeper()
    street()
    if front_is_clear(): # since the assumption is that is is a column first, and the end of the column will have right, left, and front blocked;
        city()           #this difference between 'streets' and 'city' allows for the differentiation between the two types of rectangular world 

def street(): 
    """ If rectangular world is one column tall, then checkerboard patter is created. """
    if front_is_blocked(): # a column by definition will have the very begining blocked;
        turn_left()        #
        create_lane()
        
def city():
    """ Karel creates checkerboard pattern on grid world. """
    create_lane() 
    change_lane() 
    while left_is_clear():   
        create_lane()
        change_lane()
    if right_is_clear():
        if beepers_present():
            create_lane()
        
def create_lane():
    """Creates checker pattern, is relient on beeper being placed before function runs, does not interfere with the direction of Karel"""
    while front_is_clear(): 
        if beepers_present(): 
            move()
            if front_is_clear():
                move()
                put_beeper()
        else: 
            move()
            put_beeper()

def change_lane():
    """Karel moves in a northern direction one space;
    depending if a beeper is present, Karel my merely move to the following space or move and then add a beeper;
    lastly, Karel will face in the opposite direction from the adjacent wall. """
    if front_is_blocked():
        while not_facing_north():
            turn_left()
    if front_is_clear():
        if no_beepers_present():
            move()
            put_beeper()
        else:
            move()
    if left_is_clear():
        turn_left()
    else: 
        turn_right()

def turn_right():
    """Karel makes a 90 deg turn clockwise. """
    turn_left()
    turn_left()
    turn_left()

