from strategy import Strategy
from random import randint
from math import ceil
import gym
import numpy as np

NUM_GENERATIONS = 80
NUM_STRATEGIES = 30

class geneticAlgorithm(object):
    def __init__(self):
        self.strategies = []
        for i in range(0, NUM_STRATEGIES):
            self.strategies.append(Strategy())
        self.env = gym.make('SpaceInvaders-v0')
        self.env.reset()

    def evaluateScore(self, strategy):
        observation = np.array(self.env.reset())
        score = 0
        while True:
            # self.env.render()
            observation, reward, done, info = self.env.step(strategy.calculateMove(observation))
            score += reward
            if(done):
                return score
    
    def startSimulation(self):
        for i in range(1, NUM_GENERATIONS):
            print("GENERATION: " + str(i))
            scores = []
            sumScores = 0
            for strategy in self.strategies:
                score = self.evaluateScore(strategy)
                sumScores += score
                scores.append([score, strategy])
            # Sort by descending score
            scores = sorted(scores, key = lambda x: -1 * x[0])
            print("Max: " + str(scores[0][0]))
            print("Average: " + str(sumScores / NUM_STRATEGIES))
            topStrategies = []
            breededStrategies = []
            # Get 75 percentile of strategies
            for i in range(0, ceil(NUM_STRATEGIES / 4)):
                topStrategies.append(scores[i][1])
            # Breed the top strategies
            while len(breededStrategies) + len(topStrategies) < NUM_STRATEGIES:
                index1 = randint(0, len(topStrategies))
                index2 = index1
                while(index1 == index2):
                    index2 = randint(0, len(topStrategies))
                breededStrategies.append(scores[index1][1].breed(scores[index2][1]))
            self.strategies.clear()
            self.strategies.extend(topStrategies)
            self.strategies.extend(breededStrategies)
            # Mutate resulting strategies
            for strategy in self.strategies:
                strategy.mutate()

if __name__ == '__main__':
    simulation = geneticAlgorithm()
    simulation.startSimulation()

