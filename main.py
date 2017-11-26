
from curses_wrap import wrapper, CursesWindow

from game import Game


def main(scr: CursesWindow) -> None:
    game = Game(scr)
    game.play()


if __name__ == "__main__":
    wrapper(main)
