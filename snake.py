from typing import Optional, Sequence

from curses_wrap import Pair
import direction
   

class Body:
    def __init__(self, yx: Pair, nextt: 'Optional[Body]' = None, prev: 'Optional[Body]' = None, pic: int = 0):
        self.yx = yx
        self.next = nextt
        self.prev = prev
        self.pic = pic

    def push_head(self, yx: Pair, stretch: int) -> 'Body':
        yx, self.yx = self.yx, yx
        if self.next is not None:
            return self.next.push_head(yx, stretch)
        if stretch:
            self.next = Body(yx, None, self, (self.pic + 1) % 2)
            return self.next
        return Body(yx)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, tuple):
            return self.yx == other
        assert isinstance(other, Body)
        return self.yx == other.yx


class Snake:
    def __init__(self, pos: Pair) -> None:
        self.dydx = direction.RIGHT
        self.stretch = 0
        self.tail = [Body(pos)]
        self.eaten = 0

    def direct(self, d: Optional[Pair]) -> Pair:
        if d is not None:
            is_negative = d[0] == -self.dydx[0] or d[1] == -self.dydx[1]
            if not is_negative or len(self.tail) == 1:
                self.dydx = d
        return self.dydx

    def check_status(self) -> bool:
        tail = self.get_points()
        return self.head in tail[1:]

    @property
    def head(self) -> Pair:
        return self.tail[0].yx

    def eat(self) -> None:
        self.stretch += 4

    def move(self, yx, change) -> Optional[Pair]:
        if self.dydx == direction.STOP:
            return None
        old_body = self.tail[0].push_head(yx, change and self.stretch > 0)
        if change and self.stretch > 0:
            self.stretch -= 1
            self.tail.append(old_body)
        return old_body.yx   

    def get_points(self) -> Sequence[Pair]:
        return [b.yx for b in self.tail]
