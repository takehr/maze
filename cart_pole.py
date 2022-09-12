import gym
import numpy as np
env = gym.make("CartPole-v1", render_mode="rgb_array")#render_mode="human(visible), None(default, fast), rgb_array"
env.action_space.seed(42)

observation = env.reset(seed=42)

for _ in range(1000):
    observation, reward, done, info = env.step(env.action_space.sample())
    print(observation)
#    print(np.array(env.render()).mean())

    if done:
        observation = env.reset()

env.close()