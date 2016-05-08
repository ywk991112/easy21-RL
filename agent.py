import random
from classes import Action, Card

class Agent:
    def __init__(self, sSet, aSet):
        sLen = len(sSet)
        aLen = len(aSet)
        self.sList = sSet
        self.aList = aSet
        self.QList = [[0 for action in aLen] for state in sLen]
        self.pList = [[0 for action in aLen] for state in sLen]

    def MCLearning(self, env, iter):
        for i in range(iter):
            state = env.getInitState()
            while not state.ter:
                epiEveryStep = []
                reward, nextState = env.step(state, )

    def nextAction(self, s):
        sIdx = s.index
        aNum = len(aList[sIdx])
        opActIdx = QList[sIndex].index(max(QList[sIndex]))
