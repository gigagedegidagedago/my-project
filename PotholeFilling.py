"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def main():
    """
    TODO:
    """
    pass
    for i in range(3):
        go_in()
        put_99()
        go_out()

def go_in():
    """
    pre_condition:
    Karel is at the upper left of the other side of the pothole facing East
    post_condition:
    Karel is at the pothole facing South
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre_condition:
    Karel is at the pothole facing South
    post_condition:
    Karel is at the upper left of the other side of the pothole facing East
    """
    turn_around()
    move()
    turn_right()
    move()

def turn_around():

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
