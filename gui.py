from typing import Optional, Callable, Set, Dict, Iterable
from snake import Snake
import curses_wrap as curses
from curses_wrap import Pair, CursesWindow
from random import randint

import direction

NOCHAR = -1
ESC_CHAR = 27
  
BOLD = curses.A_BOLD
NORMAL = curses.A_NORMAL
REVERSE = curses.A_REVERSE

BLACK = curses.COLOR_BLACK
BLUE = curses.COLOR_BLUE
CYAN = curses.COLOR_CYAN
GREEN = curses.COLOR_GREEN
MAGENTA = curses.COLOR_MAGENTA
RED = curses.COLOR_RED
WHITE = curses.COLOR_WHITE
YELLOW = curses.COLOR_YELLOW


def wait(delay: int) -> None:
    for _ in times:
        curses.delay_output(factor*delay)


factor: int = 25  # 5000 for textmode
times = range(1)  # 40 for textmode


def flash() -> None:
    for _ in range(4):
        curses.flash()
        curses.delay_output(50)


meaning = {
    curses.KEY_LEFT:  direction.LEFT,
    curses.KEY_RIGHT: direction.RIGHT,
    curses.KEY_UP:    direction.UP,
    curses.KEY_DOWN:  direction.DOWN,
    -1: None,
}


class Gui:
    miny: int = 1
    minx: int = 1
    maxy: int
    maxx: int
    
    def __init__(self, scr: CursesWindow) -> None:
        self.scr = scr
        curses.start_color()
        curses.curs_set(0)
        self.scr.nodelay(1)
        curses.use_default_colors()

        self.clean()
        for i in range(curses.COLORS):
            curses.init_pair(i, i, -1)
        
    def clean(self) -> None:
        self.scr.erase()
        self.maxy, self.maxx = self.scr.getmaxyx()
        self.win = self.scr.subwin(self.maxy - 2, self.maxx, 0, 0)
        self.win.border()
        self.maxy -= 4
        self.maxx -= 2
        self.statuswin = self.scr.subwin(2, self.maxx, self.maxy + 2, 0)
        self.board = [[' ' for _ in range(self.maxx)] for _ in range(self.maxy)]

    def pause(self) -> None:
        while self.scr.getch() == NOCHAR:
            pass
        
    def paint(self, brickset: Set[Pair], food: Dict[Pair, str], snake: Snake,
              old_body: Optional[Pair], eaten: int) -> None:
        self.food_paint(food)
        self.brick_paint(brickset)
             
        if old_body:
            self.addstr(old_body, ' ')
        for b in reversed(snake.tail):
            s: Optional[Pair] = b.next.yx if b.next else None
            t: Optional[Pair] = b.prev.yx if b.prev else None
            c: str = direction.get_char(s, b.yx, t, b.pic)
            self.addstr(b.yx, c,  YELLOW, BOLD)
        
        self.write_status(snake.head, len(snake.tail), eaten, len(brickset))
            
    def brick_paint(self, brickset: Set[Pair]) -> None:
        for yx in brickset:
            self.addstr(yx, '👽', RED, BOLD)
        
    def food_paint(self, food: Dict[Pair, str]) -> None:
        for yx, c in food.items():
            self.addstr(yx, c, GREEN, BOLD)
    
    def clear(self, someset: Iterable[Pair]) -> None:
        for yx in someset:
            self.addstr(yx, ' ')        
        
    @property
    def center(self) -> Pair:
        return (self.maxy // 2, self.maxx // 2)

    # noinspection PyMethodMayBeStatic
    def flash(self) -> None:
        flash()
   
    def getch(self, delay: int = 0) -> int:
        wait(delay)
        try:
            ch = self.scr.getch()
        finally:
            curses.flushinp()
        if ch == 112:
            self.pause()
        return ch
    
    def do_loop(self, func: Callable[[Optional[Pair]], int]) -> None:
        ch = NOCHAR
        delay = 0
        while ch not in (ESC_CHAR, 113):
            try: 
                delay = func(meaning[ch])
            except KeyError:
                pass
            ch = self.getch(delay)

    def add(self, yx: Pair, dydx: Pair) -> Pair:
        y = yx[0] + dydx[0]
        x = yx[1] + dydx[1]
        if y < self.miny:
            y = self.maxy
        if x < self.minx:
            x = self.maxx
        if y > self.maxy:
            y = self.miny
        if x > self.maxx:
            x = self.minx
        return (y, x)

    def write_status(self, yx: Pair, length: int, fruits: int, enemies: int) -> None:
        y, x = yx
        st = " Position: {:>2d},{:>2d} | Length: {:<3d} | Fruits: {:<2d} | Enemies: {:<4d} |  "
        fmt = st.format(y, x, length, fruits, enemies)
        self.statuswin.addstr(0, 0, fmt)
        self.statuswin.refresh()
        
    def addstr(self, yx: Pair, ch: Optional[str] = None, color: Optional[int] = None, nice: int = NORMAL) -> None:
        y, x = yx  
        att = curses.color_pair(color if color else 0) | nice
        if y >= 0 and x >= 0:
            self.scr.addch(y, x, ch, att)

    def is_out_of_bounds(self, y: int, x: int) -> bool:
        return y < self.miny or y > self.maxy or x < self.minx or x > self.maxx
    
    def random_point(self) -> Pair:
        return (randint(self.miny, self.maxy), randint(self.minx, self.maxx))
