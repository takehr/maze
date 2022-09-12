import maze
import numpy as np
import random
import matplotlib.pyplot as plt
from pprint import pprint
from queue import Queue
import copy
from tqdm import tqdm

def epsilonGreedy(Q, state, epsilon=0.2):
    a = np.argmax(Q[state[0]][state[1]])
    return random.choices([0,1,2,3], [(epsilon)/(4-1) if i!=a else 1-epsilon for i in range(4)])
def greedy(Q, state,):
    a = np.argmax(Q[state[0]][state[1]])
    return a

if __name__ == "__main__":
#    size=(12,12)
#    size=(14,14)
    size=(20,20)
    Q = np.zeros( (size[0], size[1], 4) )

    env = maze.Maze(size=size)
    random.seed()

    total_epoch=3000
    gamma=0.99

    rewards =[]

    for epoch in tqdm(range(total_epoch)):

        alpha = 0.1
        epsilon = 0.1
        la = 0.7

#------------- Try out -----------------------------
        r, state, end = copy.deepcopy(env.reset())
        trajectory = []
        trajectory.append(state)
        for _ in range(100000):
            action = copy.deepcopy(epsilonGreedy(Q, state, epsilon)[0])
            r, state, end = copy.deepcopy(env.step(action))
            trajectory.append(action)
            trajectory.append(r)
            trajectory.append(end)
            trajectory.append(state)
            if end: break

#------------- Update Q Table -----------------------
#        for i in range(10000000):
#            s=trajectory[i*4]
#            a=trajectory[1+i*4]
#            r=trajectory[2+i*4]
#            end=trajectory[3+i*4]
#
#            s_ = trajectory[4+i*4]
#
#            lambda_estimate = 0
#            rs = [ trajectory[j] for j in np.arange(2+i*4, len(trajectory), 4)]
#            for N in np.arange(len(trajectory)//4):
#                s_N_ = trajectory[(N+1)*4]
#                N_step_estimate = sum([gamma**n * r for n, r in enumerate(rs[:N+1])])\
#                     + gamma**N * Q[s_N_[0]][s_N_[1]][greedy(Q, s_N_)]
#                lambda_estimate += la**N * N_step_estimate
#
        total_step = len(trajectory)//4
        estimators = np.zeros(total_step)
        for N in np.arange(total_step)[::-1]:
            s = trajectory[N*4]
            a = trajectory[N*4+1]
            r = trajectory[N*4+2]
            s_next = trajectory[(N+1)*4]
            estimators[N] = Q[s_next[0]][s_next[1]][greedy(Q, s_next)]
            estimators*=gamma
            for i in range(N, len(estimators)):
                estimators[i]+=r*la**(i-N)
            estimators*=la
            
            Q[s[0]][s[1]][a] = Q[s[0]][s[1]][a] + alpha*(estimators.sum()*(1-la) - Q[s[0]][s[1]][a])
#            
#            lambda_estimate*= 1 - la
#
#            Q[s[0]][s[1]][a] = Q[s[0]][s[1]][a] + alpha*(lambda_estimate - Q[s[0]][s[1]][a])
#            if end:break
        rewards.append(sum([gamma**n*r for n,r, in enumerate([ trajectory[j] for j in np.arange(2, len(trajectory), 4)])]))

    pprint(env.world)
    pprint(list(np.sum(np.array(Q),axis=2)))
    plt.imshow(np.sum(np.array(Q),axis=2))
    plt.colorbar()
    plt.figure()
    plt.plot(rewards)
    plt.show()