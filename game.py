from environment import Environment
from agent import Agent, MCLearning
from classes import Action, State, Card
# test
import random

# test environment
#  e = Environment()
#  someState = State(7, 6)
#  print "********* test hit ***********"
#  while not someState.ter:
    #  someState, reward = e.step(someState, Action.hit)
    #  print
    #  print "player value: ", someState.p_value
    #  print "dealer value: ", someState.d_value
    #  print "reward      : ", reward

#  print()
#  for x in range(1, 10):
    #  someState = State(18, 10)
    #  print "********* test stick **********"
    #  someState, reward = e.step(someState, Action.stick)
    #  print "player value: ", someState.p_value
    #  print "dealer value: ", someState.d_value
    #  print "reward      : ", reward

# test monte carlo
e = Environment()
agt = Agent(e.stateSet)
mcl = MCLearning(e, agt)
mcl.evaluation(100000)


#  def checkTer(s):
    #  if s.p_value > 21 or s.p_value < 1 or s.d_value >= 17 or s.d_value < 1:
        #  return True
    #  else:
        #  return False

#  e = Environment()
#  for i in range(100000):
    #  a = e.getInitState()
    #  if a.ter:
        #  print 'fuck you'
#  for i in range(1000):
    #  a = e.getState(random.randint(1,10), random.randint(1,10), 1)
    #  print a.p_value, a.d_value
#  stateSet = e.stateSet
#  for s in stateSet:
    #  if not checkTer(s):
        #  if s.ter:
            #  print 'ERROR'


#  a = e.getState(9, 10, 1)
#  print a.p_value, a.d_value
