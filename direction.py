import itertools

UP    = (-1, 0)
DOWN  = ( 1, 0)
LEFT  = ( 0,-1)
RIGHT = ( 0, 1)
STOP  = ( 0, 0)

HORIZON = [LEFT, RIGHT]
VERT    = [UP, DOWN]
DIRECTIONS = HORIZON + VERT


UPUP    =   (UP, UP)
DOWNDOWN  = (DOWN,  DOWN)
LEFTLEFT  = (LEFT, LEFT)
RIGHTRIGHT =(RIGHT,    RIGHT)
UPLEFT =    (UP,    LEFT)
UPRIGHT =   (UP,    RIGHT)
DOWNLEFT =  (DOWN,  LEFT)
DOWNRIGHT = (DOWN,  RIGHT)
LEFTUP =    (LEFT,  UP)
RIGHTUP =   (RIGHT, UP)
LEFTDOWN =  (LEFT,  DOWN)
RIGHTDOWN = (RIGHT, DOWN)
DIC = {
    UP    : '^',
    DOWN  : 'v',
    LEFT  : '<',
    RIGHT : '>',
    STOP  : 'X',
}
TAIL = '+'
MOVEMENT = {
    UPUP      : '|',
    DOWNDOWN  : '|',
    LEFTLEFT  : '-',
    RIGHTRIGHT: '-',
    UPLEFT    : 'O',
    UPRIGHT   : 'O',
    DOWNLEFT  : 'O',
    DOWNRIGHT : 'O',
    LEFTUP    : 'O',
    RIGHTUP   : 'O',
    LEFTDOWN  : 'O',
    RIGHTDOWN : 'O',
}
MOVEMENT2 = {
    UPUP      : ';',
    DOWNDOWN  : ';',
    LEFTLEFT  : '~',
    RIGHTRIGHT: '~',
    UPLEFT    : '0',
    UPRIGHT   : '0',
    DOWNLEFT  : '0',
    DOWNRIGHT : '0',
    LEFTUP    : '0',
    RIGHTUP   : '0',
    LEFTDOWN  : '0',
    RIGHTDOWN : '0',
}

NEIGHBORS = set(itertools.product(range(-1, 2), range(-1, 2))) -{(0,0)}

def fd(new, old):
    d = new - old
    return d if abs(d) <= 1 else -d//abs(d)

def make_direction(s, t):
    return ( fd(s[0], t[0]), fd(s[1], t[1]) )

def get_char(s, me, t, i = 0):
    array = [MOVEMENT, MOVEMENT2]
    if t and s:    return array[i][
            (make_direction(s, me), make_direction(me, t))]
    if t:
        return TAIL
    if s:
        return DIC[make_direction(me, s)]
    return 'X'
