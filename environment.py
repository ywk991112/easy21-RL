import random
from classes import Action, State, Card

class Environment:

    def __init__(self):
        self.stateSet = [State(x-9,y-9,x*41+y) for x in range(41) for y in range(41)]

    def getInitState(self):
        return self.getState(random.randint(1,10), random.randint(1,10))

    def step(self, s, a):
        if a == Action.hit:
            nextCard = self.drawCard()
            nextState = self.getState(s.p_value + nextCard.value, s.d_value)
            return nextState, self.reward(nextState, False)
        elif a == Action.stick:
            #  init nextState
            nextState = self.getState(s.p_value, s.d_value)
            while not nextState.ter:
                nextCard = self.drawCard()
                nextState = self.getState(s.p_value, s.d_value + nextCard.value)
            return nextState, self.reward(nextState, True)

    # if dealer takes turn, ter = True, else ter = False, different from State.ter
    @staticmethod
    def reward(s, ter):
        #  bust
        if s.p_value > 21 or s.p_value < 1:
            return -1
        elif s.p_value > 21 or s.d_value < 1:
            return 1
        #  end of the game
        if ter:
            if s.d_value > s.p_value:
                return -1
            elif s.d_value < s.p_value:
                return 1
        #  game not yet end or draw at the end
        return 0

    @staticmethod
    def drawCard():
        value = random.randint(1, 10)
        if random.randint(1,3) == 1:
            sign = -1
        else:
            sign = 1
        return Card(sign, value)

    def getState(self, p, d):
        return self.stateSet[(p+9)*41+(d+9)]


