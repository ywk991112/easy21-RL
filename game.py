from environment import Environment
from MCLearning import MCLearning
from TDLearning import TDLearning
from LinearFuncApprox import LinearFuncApprox
import matplotlib.pyplot as plt
import numpy as np

env = Environment()



# test monte carlo
mcl = MCLearning(env)
mcl.evaluation(1000000)
mcl.plot()

# test temporal difference
tdl = TDLearning(env)
for lamb in np.arange(0, 1, 0.1):
    tdl.reset()
    tdl.Sarsa(lamb, 1000, 1)
    print 'lambda =', lamb, ', error =', tdl.msError(mcl.QList)

episodes = np.arange(0, 100000, 10000)
errLam0 = []
errLam1 = []
for epi in episodes:
    tdl.reset()
    tdl.Sarsa(0, epi, 1)
    errLam0.append(tdl.msError(mcl.QList))
    tdl.reset()
    tdl.Sarsa(1, epi, 1)
    errLam1.append(tdl.msError(mcl.QList))
plt.plot(episodes, errLam0, label="lambda = 0")
plt.plot(episodes, errLam1, label="lambda = 1")
plt.legend()
plt.xlabel('Episodes')
plt.ylabel('Mean Squared Errors')
plt.show()

# test linear function approximation
lfa = LinearFuncApprox(env)
lambda_a = np.arange(0, 1, 0.1)
err = []
for lamb in lambda_a:
    lfa.reset()
    lfa.SarsaLambLinFApp(lamb, 1000, 1)
    err.append(lfa.msError(mcl.QList))
plt.plot(lambda_a, err)
plt.legend()
plt.xlabel('lambda')
plt.ylabel('Mean Squared Errors')
plt.show()

episodes = np.arange(0, 100000, 10000)
errLam0 = []
errLam1 = []
for epi in episodes:
    lfa.reset()
    lfa.SarsaLambLinFApp(0, epi, 1)
    errLam0.append(lfa.msError(mcl.QList))
    lfa.reset()
    lfa.SarsaLambLinFApp(1, epi, 1)
    errLam1.append(lfa.msError(mcl.QList))
plt.plot(episodes, errLam0, label="lambda = 0")
plt.plot(episodes, errLam1, label="lambda = 1")
plt.legend()
plt.xlabel('Episodes')
plt.ylabel('Mean Squared Errors')
plt.show()
