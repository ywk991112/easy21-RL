from enum import Enum

class Action(Enum):
    stick = 0
    hit = 1

class Card:
    def __init__(self, s, v):
        self.value = s*v

class State:
    def __init__(self, p_v, d_v, i):
        self.index = i
        self.p_value = p_v
        self.d_value = d_v
        self.ter = checkTer(self)

def checkTer(s):
    if s.p_value > 21 or s.p_value < 1 or s.d_value >= 17 or s.d_value < 1:
        return True
    else:
        return False

