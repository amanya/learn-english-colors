#!/usr/bin/env python

import random
from os import system
import time

import argparse

colors = ['RED', 'ORANGE', 'YELLOW', 'LIGHT BLUE', 'DARK BLUE', 'SILVER', 'GREEN', 'BLACK', 'GREY', 'PURPLE', 'BROWN', 'PINK', 'GOLD', 'WHITE']

colors = [
    ('RED', '\033[48;5;1m'),
    ('ORANGE', '\033[48;5;208m'),
    ('YELLOW', '\033[48;5;11m'),
    ('LIGHT BLUE', '\033[48;5;81m'),
    ('DARK BLUE', '\033[48;5;19m'),
    ('SILVER', '\033[48;5;255m'),
    ('GREEN', '\033[48;5;2m'),
    ('BLACK', '\033[48;5;0m'),
    ('GREY', '\033[48;5;244m'),
    ('PURPLE', '\033[48;5;91m'),
    ('BROWN', '\033[48;5;52m'),
    ('PINK', '\033[48;5;13m'),
    ('GOLD', '\033[48;5;178m'),
    ('WHITE', '\033[48;5;15m'),
    ]

ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def say(text):
    system("say %s" % text.lower())

def print_colors(hide_names = False, shuffle = False, talk = False):
    pos = 0
    if shuffle:
        random.shuffle(colors)
    for color, escape in colors:
        pos = pos + 1
        print(escape + "  " + ENDC + " -> " + BOLD + ("%i" % pos if hide_names else color) + ENDC)
        if talk:
            say(color)

def test_colors(talk):
    correct_answers = 0
    random.shuffle(colors)
    for color, escape in colors:
        if talk: say(color)
        response = raw_input(escape + "  " + ENDC + " -> " + BOLD)
        print(ENDC)
        if response.lower() == color.lower():
            say("well done!")
            correct_answers = correct_answers + 1
        else:
            print("      " + BOLD + color + ENDC) 
            say("wrong")
            time.sleep(1)
            say("press enter to continue")
            raw_input()
    text = "%d correct answers of %d" % (correct_answers, len(colors))
    print(text)
    say(text)

if __name__ == '__main__':
    test_colors(True)

