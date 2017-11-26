from typing import Optional
from curses_wrap import CursesWindow, Pair
import pickle

from gui import Gui

from gameplay import Gameplay

filename = '.save.snake'


class Game:
    def __init__(self, scr: CursesWindow) -> None:
        self.delay = 0
        self.gui = Gui(scr)
        self.game = Gameplay(self.gui, self.gui.center)
        
    def load(self) -> bool:
        try:
            with open(filename, "rb") as f:
                self.game = pickle.load(f)
            return True
        except IOError:
            self.game = Gameplay(self.gui, self.gui.center)
            return False
            
    def save(self) -> None:
        with open(filename, "wb") as f:
            self.game.gui = None  # type: ignore
            pickle.dump(self.game, f)
            
    def pause(self) -> None:
        self.gui.pause()
        
    def loop(self, d: Optional[Pair]) -> int:
        self.delay = self.game.direct(d)
        if self.game.step():
            self.gui.flash()
            self.pause()
            self.game.reset()
        return self.delay
    
    def play(self) -> None:
        self.init()
        self.gui.do_loop(self.loop)
        self.save()
        
    def init(self) -> None:
        self.delay = 0
        self.gui = Gui(self.gui.scr)

        ok = self.load()
        self.game.gui = self.gui
        if not ok:
            self.game.reset()
        assert self.game.snake is not None
