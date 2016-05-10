from environment import Environment
from MCLearning import MCLearning
# test
import random

# test monte carlo
e = Environment()
mcl = MCLearning(e)
mcl.evaluation(1000000)
