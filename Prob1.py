#====================================================
# Filename: Prob2.py
# 
# Your name: Nathan G. Diaz
# Who did you work with (if anyone)?:
# Estimate for time spent (in hrs)?: 4
#====================================================

import karel

# Your program should create a checkerboard pattern on any
# rectangular world. I am defining a few functions below to
# get you started, but you can (and should) add whatever
# other helper functions you want below.

def create_checkerboard():
    """ Main function to create the checkerboard pattern. """
    put_beeper()
    isColumn()
    isGrid()

def isColumn():
    if front_is_blocked():
        turn_left()
        create_lane()


def isGrid():
    create_lane()
    if front_is_clear:
        create_lane()
        create_lane()
    else: create_lane()
   

def create_lane():
    while front_is_clear():
         move()
         if front_is_clear():
            move()
            put_beeper()
    change_lane()

def change_lane():
    if front_is_blocked():
        while not_facing_north():
            turn_left()
        move()
        if right_is_blocked():
            turn_left()
            if right_is_clear():
                turn_right()

        