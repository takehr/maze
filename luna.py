import gym
env = gym.make("LunarLander-v2", render_mode="human")
env.action_space.seed(42)

observation = env.reset(seed=42)

for _ in range(1000):
    observation, reward, done, info = env.step(env.action_space.sample())
    print(observation)

    if done:
        observation = env.reset()

env.close()

#import numpy as np
#import gym
#from gym.utils.play import play
#play(gym.make("CartPole-v1"), keys_to_action={
#                                               "a": np.array(0),
#                                               "d": np.array(1),
#                                              }, noop=np.array(0))
#import numpy as np
#import gym
#from gym.utils.play import play
#play(gym.make("CarRacing-v2"), keys_to_action={
#                                               "w": np.array([0, 0.7, 0]),
#                                               "a": np.array([-1, 0, 0]),
#                                               "s": np.array([0, 0, 1]),
#                                               "d": np.array([1, 0, 0]),
#                                               "wa": np.array([-1, 0.7, 0]),
#                                               "dw": np.array([1, 0.7, 0]),
#                                               "ds": np.array([1, 0, 1]),
#                                               "as": np.array([-1, 0, 1]),
#                                              }, noop=np.array([0,0,0]))