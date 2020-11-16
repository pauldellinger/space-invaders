from geneticAlgo import geneticAlgorithm
import sys
import gym
import numpy as np
from strategy import Strategy
import os.path

def playback(filename):
    strategy = Strategy.load_strategy(os.path.join('strategies', filename))
    env = gym.make('SpaceInvaders-v0')
    env.seed(0)
    while True:
        env.reset()
        observation = np.array(env.reset())
        env.seed(0)
        score = 0
        while True:
            env.render()
            observation, reward, done, info = env.step(strategy.calculateMove(observation))
            score += reward
            if(done):
                print(score)
                break


if __name__ == "__main__":
    print(sys.argv)
    playback(sys.argv[1])