from collections import defaultdict
from environment import Action
import matplotlib.pyplot as plt
import numpy as np
import random

class TDLearning:
    def __init__(self, env):
        self.QList = defaultdict(float) #(s, a)
        self.EList = defaultdict(float) #(s, a)
        self.NList = defaultdict(int) #(s, a)
        self.env = env

    def Sarsa(self, lamb, iter, gamma):
        for i in range(iter):
            self.EList.clear()
            curState = self.env.getInitState()
            curAction = self.epsilonGreedy(curState)
            while curState:
                for (s, a) in self.EList:
                    self.EList[(s, a)] = self.EList[(s, a)] * gamma
                self.EList[(curState, curAction)] += 1
                self.visit(curState, curAction)
                nextState, reward = self.env.step(curState, curAction)
                nextAction = self.epsilonGreedy(nextState)
                tdError = reward + gamma * self.QList[(nextState, nextAction)] - self.QList[(curState, curAction)]
                for (s, a) in self.EList:
                    self.QList[(s, a)] = self.QList[(s, a)] + self.alpha(s, a) * tdError * self.EList[(s, a)]
                curState, curAction = nextState, nextAction

    def reset(self):
        self.QList.clear()
        self.EList.clear()
        self.NList.clear()

    def error(self, realQList):
        error = 0
        for i in range(22):
            for j in range(11):
                for a in (Action.stick, Action.hit):
                    error += (self.QList[(i, j), a] - realQList[(i, j), a]) **2
        return error

    def alpha(self, state, action):
        return 1. / self.NList[state, action]

    def epsilonGreedy(self, s):
        optAction = None
        if self.QList[s, Action.hit] < self.QList[s, Action.stick]:
            optAction = Action.stick
        else:
            optAction = Action.hit
        epsilon = 100. / (100. + (self.NList[s]))
        if random.random() < epsilon:
            return random.choice([Action.hit, Action.stick])
        else:
            return optAction

    def visit(self, s, a):
        self.NList[s] += 1
        self.NList[s, a] += 1
