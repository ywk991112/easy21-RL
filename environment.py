import random
from enum import Enum

class Action(Enum):
    stick = 0
    hit = 1

class Environment:

    def getInitState(self):
        return (random.randint(1,10), random.randint(1,10))

    def step(self, s, a):
        if a == Action.hit:
            nextCard = self.drawCard()
            nextState = (s[0] + nextCard, s[1])
            return self.terCheck(nextState), self.reward(nextState, False)
        elif a == Action.stick:
            #  init nextState
            nextState = s
            while self.terCheck(nextState):
                nextCard = self.drawCard()
                nextState = (nextState[0], nextState[1] + nextCard)
            return self.terCheck(nextState), self.reward(nextState, True)

    # if dealer takes turn, ter = True, else ter = False, different from State.ter
    @staticmethod
    def reward(s, ter):
        #  bust
        if s[0] > 21 or s[0] < 1:
            return -1
        elif s[1] > 21 or s[1] < 1:
            return 1
        #  end of the game
        if ter:
            if s[0] > s[1]:
                return 1
            elif s[0] < s[1]:
                return -1
        #  game not yet end or draw at the end
        return 0

    @staticmethod
    def drawCard():
        value = random.randint(1, 10)
        sign = random.choice([1, 1, -1])
        return sign * value

    @staticmethod
    def terCheck(s):
        if s[0] > 21 or s[0] < 1 or s[1] >= 17 or s[1] < 1:
            return None
        else:
            return s

