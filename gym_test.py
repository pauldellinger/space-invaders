import gym
import numpy as np
env = gym.make('SpaceInvaders-v0')
env.reset()
print(np.array(env.reset()).flatten())
print(env.action_space)
print(env.observation_space)
while True:
    env.render()
    # print(env.action_space.sample())
    env.step(env.action_space.sample())
