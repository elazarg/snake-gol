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


def delay_output(delay: int) -> None:
    curses.delay_output(delay)


def color_pair(n: int) -> int:
    return curses.color_pair(n)


def start_color() -> None:
    curses.start_color()  # type: ignore


def init_pair(i: int, x: int, z: int) -> None:
    curses.init_pair(i, x, z)


def curs_set(n: int) -> None:
    curses.curs_set(n)


def flash() -> None:
    curses.flash()


def use_default_colors() -> None:
    curses.use_default_colors()


def flushinp() -> None:
    curses.flushinp()


def wrapper(func: typing.Callable[['CursesWindow'], None]) -> None:
    curses.wrapper(func)  # type: ignore


KEY_LEFT = curses.KEY_LEFT
KEY_RIGHT = curses.KEY_RIGHT
KEY_UP = curses.KEY_UP
KEY_DOWN = curses.KEY_DOWN


# noinspection PyMethodMayBeStatic
class CursesWindow:
    def getch(self) -> int: return 0

    def subwin(self, _y: int, _x: int, _yy: int, _xx: int) -> 'CursesWindow': return self

    def getmaxyx(self) -> Pair: return (0, 0)

    def border(self) -> Pair: return (0, 0)

    def nodelay(self, n: int) -> None: pass

    def erase(self) -> None: pass

    def addstr(self, y: int, x: int, text: str) -> None: pass

    def addch(self, y: int, x: int, ch: typing.Optional[str], color: int) -> None: pass

    def refresh(self) -> None: pass
