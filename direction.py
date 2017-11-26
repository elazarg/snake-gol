from typing import Optional
from curses_wrap import Pair
import itertools

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
STOP = (0, 0)

HORIZON = (LEFT, RIGHT)
VERT = (UP, DOWN)
DIRECTIONS = HORIZON + VERT

UPUP = (UP, UP)
DOWNDOWN = (DOWN, DOWN)
LEFTLEFT = (LEFT, LEFT)
RIGHTRIGHT = (RIGHT, RIGHT)
UPLEFT = (UP, LEFT)
UPRIGHT = (UP, RIGHT)
DOWNLEFT = (DOWN, LEFT)
DOWNRIGHT = (DOWN, RIGHT)
LEFTUP = (LEFT, UP)
RIGHTUP = (RIGHT, UP)
LEFTDOWN = (LEFT, DOWN)
RIGHTDOWN = (RIGHT, DOWN)
DIC = {
    UP: '△',
    DOWN: '▽',
    LEFT: '◁',
    RIGHT: '▷',
    STOP: 'X',
}
TAIL = '+'
MOVEMENT = {
    UPUP: '|',
    DOWNDOWN: '|',
    LEFTLEFT: '~',
    RIGHTRIGHT: '~',
    UPLEFT: '╮',
    UPRIGHT: '╭',
    DOWNLEFT: '╯',
    DOWNRIGHT: '╰',
    LEFTUP: '╰',
    RIGHTUP: '╯',
    LEFTDOWN: '╭',
    RIGHTDOWN: '╮',
}
MOVEMENT2 = {
    UPUP: ':',
    DOWNDOWN: ':',
    LEFTLEFT: '-',
    RIGHTRIGHT: '-',
    UPLEFT: '╮',
    UPRIGHT: '╭',
    DOWNLEFT: '╯',
    DOWNRIGHT: '╰',
    LEFTUP: '╰',
    RIGHTUP: '╯',
    LEFTDOWN: '╭',
    RIGHTDOWN: '╮',
}

NEIGHBORS = set(itertools.product(range(-1, 2), range(-1, 2))) - {(0, 0)}


def fd(new: int, old: int) -> int:
    d = new - old
    return d if abs(d) <= 1 else -d // abs(d)


def make_direction(s: Pair, t: Pair) -> Pair:
    return (fd(s[0], t[0]), fd(s[1], t[1]))


def get_char(s: Optional[Pair], me: Optional[Pair], t: Optional[Pair], i: int = 0) -> str:
    array = [MOVEMENT, MOVEMENT2]
    if t and s:
        return array[i][(make_direction(me, t), make_direction(s, me))]
    if t:
        return TAIL
    if s:
        y, x = make_direction(me, s)
        return DIC[(y, x)]
    return 'X'
