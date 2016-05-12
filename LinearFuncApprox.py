from collections import defaultdict
from environment import Action
import matplotlib.pyplot as plt
import numpy as np
import random

class LinearFuncApprox:
    def __init__(self, env):
        self.QList = defaultdict(float) #(s, a)
        self.EList = defaultdict(float) #(s, a)
        self.theta = np.zeros(shape=(3, 6, 2))
        self.env = env

    def SarsaLambLinFApp(self, lamb, iter, gamma):
        for i in range(iter):
            self.EList.clear()
            curState = self.env.getInitState()
            curAction = self.epsilonGreedy(curState)
            while curState:
                for (s, a) in self.EList:
                    self.EList[(s, a)] = self.EList[(s, a)] * gamma
                self.EList[(curState, curAction)] += 1
                nextState, reward = self.env.step(curState, curAction)
                nextAction = self.epsilonGreedy(nextState)
                tdError = reward + gamma * self.getValue(nextState, nextAction) - self.getValue(curState, curAction)
                alpha = 0.01
                for (s, a) in self.EList:
                    self.theta += alpha * tdError * (self.EList[(s, a)] * self.getFeature(s, a))
                curState, curAction = nextState, nextAction

    def msError(self, realQList):
        error = 0
        for i in range(22):
            for j in range(11):
                for a in (Action.stick, Action.hit):
                    error += (self.getValue((i, j), a) - realQList[(i, j), a]) **2
        return error

    def getValue(self, s, a):
        if not s:
            return 0
        return np.sum(self.theta * self.getFeature(s, a))  # ?

    def getFeature(self, s, a):
        phi = np.zeros((3, 6, 2))
        d_i = [(1, 4), (4, 7), (7, 10)]
        p_i = [(1, 6), (4, 9), (7, 12), (10, 15), (13, 18), (16, 21)]
        aIdx = 1 if a == Action.hit else 0
        for dIdx, d_itv in enumerate(d_i):
            if not d_itv[0] <= s[1] <= d_itv[1]:
                continue
            for pIdx, p_itv in enumerate(p_i):
                if p_itv[0] <= s[0] <= p_itv[1]:
                    phi[dIdx][pIdx][aIdx] += 1
        return phi

    def reset(self):
        self.QList.clear()
        self.EList.clear()

    def epsilonGreedy(self, s):
        optAction = None
        if self.QList[s, Action.hit] < self.QList[s, Action.stick]:
            optAction = Action.stick
        else:
            optAction = Action.hit
        epsilon = 0.05
        if random.random() < epsilon:
            return random.choice([Action.hit, Action.stick])
        else:
            return optAction

