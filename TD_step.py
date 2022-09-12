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
    size=(20,20)
    Q = np.zeros( (size[0], size[1], 4) )

    env = maze.Maze(size=size, seed=8093)

    total_epoch=10000
    #alpha = 0.01
    gamma=0.99

    revenue = []

    for epoch in range(total_epoch):

        #epsilon= (1-epoch/total_epoch)**5
        #alpha = 1/(epoch+1)
        alpha = 0.1
        epsilon = 0.1
        rewards=[]

#------------- Try out -----------------------------
        r, state, end = copy.deepcopy(env.reset())
        rewards.append(r)
        
        for _ in range(100000):
            action = copy.deepcopy(epsilonGreedy(Q, state, epsilon)[0])
            r, state_, end = copy.deepcopy(env.step(action))
            rewards.append(r)
#------------- Update Q Table -----------------------
            estimate = r + gamma*Q[state_[0]][state_[1]][greedy(Q, state_)]
            Q[state[0]][state[1]][action] = Q[state[0]][state[1]][action] + alpha*(estimate - Q[state[0]][state[1]][action])
            state=state_
            if end: break
        revenue.append(sum([gamma**n*r for n,r, in enumerate(rewards)]))

    pprint(env.world)
    pprint(list(np.sum(np.array(Q),axis=2)))
    plt.imshow(np.sum(np.array(Q),axis=2))
    plt.colorbar()
    plt.figure()
    plt.plot(revenue)
    plt.show()