from typing import Set, Optional

from itertools import chain

from collections import Counter
from random import randrange

from curses_wrap import Pair
from snake import Snake
import direction
from gui import Gui


class Collision(Exception):
    pass


def make_fruit() -> str:
    return chr(randrange(0x1F345, 0x1F354))


class Gameplay:
    brickset: Set[Pair]

    def __init__(self, gui: Gui, center: Pair) -> None:
        self.gui = gui
        self.center = center
        self.brickset = set()
        self.eaten = 0
        self.food = {center: chr(0x1F34E)}
        self.snake = Snake(center)

    def direct(self, d: Optional[Pair]) -> int:
        return 2 if self.snake.direct(d) in direction.HORIZON else 3

    def reset(self) -> None:
        self.eaten = 0
        if self.snake is not None:
            self.gui.clear(self.snake.get_points())
        self.snake = Snake(self.center)

    c: int = 0
    MAX_BRICKS: int = 20

    def live_step(self) -> None:
        d = Counter([(0, 0)])
        d.clear()
        for yx in self.brickset:
            d.update(self.gui.add(yx, ij) for ij in direction.NEIGHBORS)
                
        for yx in self.snake.get_points():
            d.update(self.gui.add(yx, z) for z in [(0, -1), (0, 1), (-1, 0), (1, 0)])
                                
        old = self.brickset
        self.brickset = {yx for yx, v in d.items()
                         if v == 3 or v == 2 and yx in self.brickset}
        self.brickset -= set(self.snake.get_points())
        self.brickset -= set(self.food)
        
        self.gui.clear(old - self.brickset)

    def eat(self) -> None:
        self.snake.eat()
        self.eaten += 1                
        while True:
            yx = self.gui.random_point()
            tail = [x.yx for x in self.snake.tail]
            if yx not in tail and yx not in self.brickset:
                self.food[yx] = make_fruit()
                break
            
    def step(self) -> bool:
        head = self.snake.tail[0].yx
        if head in self.food:
            del self.food[head]
            self.eat()
                
        pos = self.gui.add(head, self.snake.dydx)
        old_body = self.snake.move(pos, self.c % 5 == 0)
        self.c += 1
        
        if self.c % 8 == 0:
            self.live_step()
            
        self.gui.paint(self.brickset, self.food, self.snake, old_body, self.eaten)
        
        return self.snake.check_status() or self.snake.head in self.brickset

