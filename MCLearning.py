import random
import numpy as np
from collections import defaultdict
from environment import Action
#graph
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

class MCLearning:
    def __init__(self, env):
        self.env = env
        self.VList = defaultdict(float) # (s)
        self.QList = defaultdict(float) # (s, a)
        self.NList = defaultdict(int) # (s, a) or (s)

    def evaluation(self, iter):
        for i in range(iter):
            # init current state
            curState = self.env.getInitState()
            episodes = []
            #  reward = 0 # test
            while curState:
                action = self.epsilonGreedy(curState)
                #  print'aIdx:', aIdx
                #  print curState, action
                nextState, reward = self.env.step(curState, action)
                episodes.append((curState, action, reward))
                self.visit(curState, action)
                curState = nextState
                #  print 'haha'
            self.everyVisitMC(episodes, 1)
            # test
            #  self.checkEpisodes(episodes)
            #  print 'end'

        self.updateV()
        self.plot()
        # test
        #  print self.VList
        #  print self.QList
        #  print self.NList

    ##############################
    #  functions for evaluation  #
    ##############################
    def everyVisitMC(self, epi, gamma):
        sum = 0
        for state, action, reward in reversed(epi):
            sum = reward + gamma * sum
            self.QList[state, action] += self.alpha(state, action) * (sum - self.QList[state, action])
            # test
            #  if state[0] > 10:
                #  print state
                #  print 'alpha', self.alpha(state, action)
                #  print 'q    ', self.QList[state, action]
                #  print 'sum  ',sum


    def alpha(self, state, action):
        #  print 'N    ', self.NList[state, action]
        #  print 'NList', self.NList
        #  print 'alpha', 1. / self.NList[state, action]
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

    def updateV(self):
        for i in range(1, 22):
            for j in range(1, 22):
                self.VList[i, j] = max(self.QList[(i, j), Action.stick], self.QList[(i, j), Action.hit])

    def plot(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        X = np.arange(1, 11, 1)
        Y = np.arange(1, 22, 1)
        X, Y = np.meshgrid(X, Y)
        V = np.zeros(X.shape)

        for i in range(1, 11):
            for j in range(1, 22):
                V[j-1, i-1] = self.VList[j, i]
        #  print self.QList
        #  print self.VList
        #  print V

        surf = ax.plot_surface(X, Y, V, rstride=1, cstride=1, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)
        ax.set_zlim(-1.01, 1.01)

        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()


    ########################
    #  functions for test  #
    ########################
    def checkEpisodes(self, epi):
        for state, action, reward in epi:
            print state, action, reward
