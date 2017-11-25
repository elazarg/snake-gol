'''
Created on May 6, 2013

@author: elazar
'''

class CircArray(tuple):
    def __new__ (cls, arg, default=None):
        if isinstance(arg, int):
            arg = [default for _ in range(arg)]
        return super().__new__(cls, [[i] for i in arg])

    def __getitem__(self, i):
        return super().__getitem__(i % len(self))[0]

    def __setitem__(self, i, v):
        super().__getitem__(i % len(self))[0] = v
    
    def __repr__(self):
        return repr([i[0] for i in self])

    def setall(self, v=None):
        for cell in self:
            cell[0]=v



class Torus(tuple):
    def __new__ (cls, leny, lenx, default=None):
        return super().__new__(cls, [CircArray([default for _ in range(lenx)]) for _ in range(leny)])

    def __getitem__(self, yx):
        return super().__getitem__(yx[0] % len(self))[yx[1]]

    def __setitem__(self, yx, v):
        super().__getitem__(yx[0] % len(self))[yx[1]] = v
    
    def setall(self, v=None):
        for line in self:
            line.setall(v)

