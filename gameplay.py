'''
Created on May 21, 2013

@author: elazar
'''
from collections import Counter
from random import randrange

from snake import Snake
import direction
  
class Collision(Exception):
    __init__ = Exception.__init__


def make_fruit():
    return chr(randrange(0x1F345, 0x1F354))


class Gameplay: 
    def __init__(self):
        self.brickset = set()
        self.food = {}
        self.snake = None

    def direct(self, d):
        return 2 if self.snake.direct(d) in direction.HORIZON else 3

    def reset(self):
        self.eaten = 0
        if self.snake:
            self.gui.clear(self.snake.get_points())
        self.snake = Snake(self.gui.center)
        if not self.food:
            self.food[self.gui.center] = chr(0x1F34E)
        
    c=0
    MAXBRICKS = 20
    def live_step(self):
        d = Counter()
        for yx in self.brickset:
            d.update(self.gui.add(yx, ij) for ij in direction.NEIGHBORS)
                
        for yx in self.snake.get_points():
            d.update(self.gui.add(yx, z) for z in [(0, -1), (0, 1), (-1, 0), (1, 0)])
                                
        old = self.brickset
        self.brickset = { yx for yx, v in d.items()
                        if v == 3 or v == 2 and yx in self.brickset }
        self.brickset -= set(self.snake.get_points())
        self.brickset -= set(self.food)
        
        self.gui.clear(old - self.brickset)

    def eat(self):
        self.snake.eat()
        self.eaten += 1                
        while True:
            yx = self.gui.random_point()
            if yx not in [x.getyx() for x in self.snake.tail] and yx not in self.brickset :
                self.food[yx] = make_fruit()
                break
            
    def step(self):
        head = self.snake.tail[0].getyx()
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

