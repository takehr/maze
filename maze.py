import random
from pprint import pprint

"""docstring
description
1 1 1 1 1 1 1 1 1 1 
1 0 0 0 0 0 0 0 g 1
1 0 0 0 0 0 0 0 0 1
1 0 1 0 0 0 0 0 0 1
1 0 0 0 1 0 0 0 0 1
1 0 1 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 1 0 0 0 0 0 0 1
1 s 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 
"""

class Maze:
    n=0
    state=[0,0]
    world=0
    start =0
    goal=0
    size=0

    def __init__(self, start=(1,1), goal=(6,6), size=(8,8), end=100, seed=0):

        random.seed(seed)

        self.start=start
        self.goal=goal
        self.state[0]=start[0]
        self.state[1]=start[1]
        self.size=size

        for _ in range(100000):
            self.world = [ [ 1 if i==0 or i==size[1]-1 or j==0 or j==size[0]-1 else 0 for i in range(size[1])] for j in range(size[0])]
            for _ in range(size[0]*size[1]//4): self.world[random.randint(1,size[0]-2)][random.randint(1,size[1]-2)]=1
            if self.check(): return
        raise Exception

    def reset(self):
        self.state[0]=self.start[0]
        self.state[1]=self.start[1]
        self.n=0

    def step(self, action):
        """
        input: 
            0: up
            1: down
            2: right
            3: left

        return:
            (r, s, end)
        """

        if self.n>=100: raise Exception

        if action == 0:
            if self.world[self.state[0]+1][self.state[1]]==0:
                self.state[0]+=1
        if action == 1:
            if self.world[self.state[0]-1][self.state[1]]==0:
                self.state[0]+=-1
        if action == 2:
            if self.world[self.state[0]][self.state[1]+1]==0:
                self.state[1]+=1
        if action == 3:
            if self.world[self.state[0]][self.state[1]-1]==0:
                self.state[1]+=-1

        if self.state[0]==self.goal[0] and self.state[1]==self.goal[1]:
            return 100, self.state, True

        self.n+=1
        if self.n == 100:
            return -1, self.state, True

        return -1, self.state, False

    def check(self):
        assert self.world
        if self.world[self.start[0]][self.start[1]]==1 or self.world[self.goal[0]][self.goal[1]]==1 : return False
        from queue import Queue
        queue = Queue()
        queue.put(self.start)
# This becomes shallow copy:   dp = [ [False]*self.size[1] ]*self.size[0]
        dp = [ [False]*self.size[1] for _ in range(self.size[0])]
        for _ in range(10000000):
            if queue.empty(): 
                return False
            s = queue.get()
            if s[0]==self.goal[0] and s[1]==self.goal[1]:return True
            dp[s[0]][s[1]]=True
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if self.world[s[0]+x][s[1]+y]==0 and dp[s[0]+x][s[1]+y]==False: queue.put( (s[0]+x, s[1]+y) )
        return False

if __name__ == "__main__":
    maze = Maze(start=(1,1), goal=(18,18), size=(20,20))
    pprint(maze.world,)
    for _ in range(100):
        print(maze.step(random.randint(0,3)))
    maze.reset()
    for _ in range(100):
        print(maze.step(random.randint(0,3)))

