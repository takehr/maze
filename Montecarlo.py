import maze
import numpy as np
import random
import matplotlib.pyplot as plt
from pprint import pprint
from queue import Queue
import copy

def epsilonGreedy(Q, state, epsilon=0.2):
    a = np.argmax(Q[state[0]][state[1]])
    return random.choices([0,1,2,3], [(epsilon)/(4-1) if i!=a else 1-epsilon for i in range(4)])
def greedy(Q, state,):
    a = np.argmax(Q[state[0]][state[1]])
    return a

if __name__ == "__main__":
    size=(14,14)
    Q = np.zeros( (size[0], size[1], 4) )

    env = maze.Maze(size=size)
    #random.seed()

    total_epoch=1000
    alpha = 0.1
    gamma=0.99

    rewards =[]

    for epoch in range(total_epoch):

        #epsilon= (1-epoch/total_epoch)**5
        epsilon = 0.2

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
        for i in range(10000000):
            s=trajectory[i*4]
            a=trajectory[1+i*4]
            r=trajectory[2+i*4]
            end=trajectory[3+i*4]
            estimate = sum([r*gamma**n for n,r, in enumerate([ trajectory[j] for j in np.arange(2+i*4,len(trajectory), 4)])])
            Q[s[0]][s[1]][a] = Q[s[0]][s[1]][a] + alpha*(estimate - Q[s[0]][s[1]][a])
            if end:break
        rewards.append(sum([gamma**n*r for n,r, in enumerate([ trajectory[j] for j in np.arange(2, len(trajectory), 4)])]))

    pprint(env.world)
    pprint(list(np.sum(np.array(Q),axis=2)))
    plt.imshow(np.sum(np.array(Q),axis=2))
    plt.colorbar()
    plt.figure()
    plt.plot(rewards)
    plt.show()