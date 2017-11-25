#!/usr/bin/python3

import direction
   

class _Body:    
    def __init__(self, yx, nextt=None, prev=None, pic = 0):
        self.yx = yx
        self.next = nextt
        self.prev = prev
        self.pic = pic

    def getyx(self):
        return self.yx

    def push_head(self, yx, stretch):
        yx, self.yx = self.yx, yx
        if self.next is not None:
            return self.next.push_head(yx, stretch)
        if stretch:
            self.next = Snake.Body(yx, None, self, (self.pic + 1) % 2)
            return self.next
        return Snake.Body(yx)

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.yx == other
        return self.yx == other.yx


class Snake:
    Body = _Body

    def __init__(self, pos):
        self.dydx = direction.RIGHT
        self.stretch = 0
        self.tail = [Snake.Body(pos)]
        self.eaten = 0

    def direct(self, d):
        if d is not None:
            is_negative = d[0] == -self.dydx[0] or d[1] == -self.dydx[1]
            if not is_negative or len(self.tail) == 1:
                self.dydx = d
        return self.dydx

    def check_status(self):
        tail = self.get_points()
        return self.head in tail[1:]

    @property
    def head(self):
        return self.tail[0].getyx()

    def eat(self):
        self.stretch += 4

    def move(self, yx, change):
        if self.dydx == direction.STOP:
            return None
        old_body = self.tail[0].push_head(yx, change and self.stretch > 0)
        if change and self.stretch > 0:
            self.stretch -= 1
            self.tail.append(old_body)
        return old_body.yx   

    def get_points(self):
        return [b.getyx() for b in self.tail]

