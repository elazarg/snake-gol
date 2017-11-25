#!/bin/python3

from curses_wrap import wrapper
from game import Game
import gui

import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            gui.factor = int(sys.argv[1])
        if len(sys.argv) > 2:
            gui.times = range(int(sys.argv[2]))
    except:
        pass
    for i in sys.argv[3:]: exec(i)

    main = Game('new' in sys.argv)
    wrapper(main.play)

