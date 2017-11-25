'''
Created on May 21, 2013

@author: elazar
'''

import pickle

from gui import Gui

from gameplay import Gameplay

filename = '.save.snake'


class Game:

    def __init__(self, isnew):
        self.isnew = isnew
        
    def load(self):
        try:
            with open(filename, "rb") as f:
                self.game = pickle.load(f)
            return True
        except:
            self.game = Gameplay()
            return False
            
    def save(self):
        with open(filename, "wb") as f:
            self.game.gui = None
            pickle.dump(self.game, f)
            
    def pause(self):
        self.gui.pause()
        
    def loop(self, d): 
        self.delay = self.game.direct(d)
        if self.game.step():
            self.gui.flash()
            self.pause()
            self.game.reset()
            #self.init(True)
        return self.delay
    
    def play(self, scr):
        self.init(self.isnew, scr)
        self.gui.do_loop(self.loop)
        self.save()
        
    def init(self, new, scr=None):
        self.delay = 0
        self.gui = Gui(scr if scr else self.gui.scr)
        if new:
            self.game = Gameplay()
            self.game.gui = self.gui
            self.game.reset()
        else:
            ok = self.load()
            self.isnew = False
            self.game.gui = self.gui
            if not ok:
                self.game.reset()
        assert self.game.snake != None

