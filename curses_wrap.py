import curses
import typing

Pair = typing.Tuple[int, int]

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
start_color = curses.start_color
init_pair = curses.init_pair
curs_set = curses.curs_set
flash = curses.flash
use_default_colors = curses.use_default_colors
flushinp = curses.flushinp
wrapper = curses.wrapper

KEY_LEFT = curses.KEY_LEFT
KEY_RIGHT = curses.KEY_RIGHT
KEY_UP = curses.KEY_UP
KEY_DOWN = curses.KEY_DOWN


class CursesWindow:
    def getch(self) -> str: return ''

    def subwin(self, _y: int, _x: int, _yy: int, _xx: int) -> 'CursesWindow': return self

    def getmaxyx(self) -> Pair: return (0, 0)

    def border(self) -> Pair: return (0, 0)

    def nodelay(self, n: int) -> None: pass

    def erase(self) -> None: pass

    def addstr(self, y: int, x: int, text: str) -> None: pass

    def addch(self, y: int, x: int, ch: str, color: int) -> None: pass

    def refresh(self) -> None: pass


del curses
