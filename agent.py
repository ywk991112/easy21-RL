import random
from classes import Action, Card

class Agent:
    def __init__(self, sSet):
        self.sList = sSet
        self.sLen = len(sSet)
        self.aList = []
        for i in range(self.sLen):
            actions = [Action.stick, Action.hit]
            self.aList.append(actions)

class MCLearning:
    def __init__(self, env, agt):
        self.agt = agt
        self.env = env
        self.VList = [ 0 for j in range(agt.sLen) ]
        self.QList = [[0 for i in range(len(agt.aList[j]))] for j in range(agt.sLen)]
        self.PList = [[0 for i in range(len(agt.aList[j]))] for j in range(agt.sLen)]
        self.NList = [[0 for i in range(len(agt.aList[j]))] for j in range(agt.sLen)]

    def evaluation(self, iter):
        #  count = 0
        for i in range(iter):
            # init current state
            curState = self.env.getInitState()
            #  print curState.p_value, curState.d_value
            episodes = []
            reward = 0 # test
            while not curState.ter:
                aIdx = self.epsilonGreedy(curState)
                print'aIdx:', aIdx
                self.NList[curState.index][aIdx] += 1
                #  count += 1
                action = self.agt.aList[curState.index][aIdx]
                nextState, reward = self.env.step(curState, action)
                episodes.append((curState.index, action, reward))
                curState = nextState
            self.everyVisitMC(episodes, 1)
            # test
            self.checkEpisodes(episodes)
            print curState.p_value, curState.d_value
            print 'reward:', reward
            print 'end'

        for i in range(self.agt.sLen):
            self.VList[i] = max(self.QList[i])

        #  print count
        #  for v in self.VList:
            #  print v
        #  for n in self.NList:
            #  print n


    ##############################
    #  functions for evaluation  #
    ##############################
    def everyVisitMC(self, epi, gamma):
        sum = 0
        for sIdx, aIdx, reward in reversed(epi):
            sum = reward + gamma * sum
            self.QList[sIdx][aIdx] += self.alpha(sIdx, aIdx) * (sum - self.QList[sIdx][aIdx])
            #  if self.QList[sIdx][aIdx]:
                #  print self.QList[sIdx][aIdx]

    def alpha(self, sIdx, aIdx):
        return float(1) / self.NList[sIdx][aIdx]

    # return action index in s
    def epsilonGreedy(self, s):
        sIdx = s.index
        aNum = len(self.agt.aList[sIdx])
        # argMax index for Q
        opActIdx = self.QList[sIdx].index(max(self.QList[sIdx]))
        #  print 'opActIdx: ', opActIdx
        if random.random() < self.epsilon(sIdx):
            return random.randint(0, aNum-1)
        else:
            return opActIdx

    def epsilon(self, sIdx):
        N0 = 100
        return float(N0) / (N0 + sum(self.NList[sIdx]))

    ########################
    #  functions for test  #
    ########################
    def checkEpisodes(self, epi):
        for state, action, reward in epi:
            s = self.env.stateSet[state]
            print s.p_value, s.d_value
