'''
Created on May 21, 2013

@author: elazar

This is an IDE-helper. it makes the names of the module variable statically visible.
'''
import curses
from curses import *

A_BOLD = curses.A_BOLD
A_NORMAL = curses.A_NORMAL
A_REVERSE = curses.A_REVERSE

COLOR_BLACK = curses.COLOR_BLACK
COLOR_BLUE = curses.COLOR_BLUE
COLOR_CYAN = curses.COLOR_CYAN
COLOR_GREEN = curses.COLOR_GREEN
COLOR_MAGENTA = curses.COLOR_MAGENTA
COLOR_RED = curses.COLOR_RED
COLOR_WHITE = curses.COLOR_WHITE
COLOR_YELLOW = curses.COLOR_YELLOW

COLORS = 8

delay_output = curses.delay_output
color_pair = curses.color_pair
init_pair = curses.init_pair

curs_set = curses.curs_set

flash = curses.flash
use_default_colors = curses.use_default_colors

flushinp = curses.flushinp

KEY_LEFT = curses.KEY_LEFT
KEY_RIGHT = curses.KEY_RIGHT
KEY_UP = curses.KEY_UP
KEY_DOWN = curses.KEY_DOWN