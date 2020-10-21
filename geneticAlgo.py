from strategy import Strategy
from spaceinvaders import SpaceInvaders
from random import randint
from math import ceil

NUM_GENERATIONS = 10
NUM_STRATEGIES = 5

class geneticAlgorithm(object):
    def __init__(self):
        self.strategies = []
        for i in range(0, NUM_STRATEGIES):
            self.strategies.append(Strategy())
    
    def startSimulation(self):
        for i in range(0, NUM_GENERATIONS):
            scores = []
            for strategy in self.strategies:
                game = SpaceInvaders(strategy)
                score = game.main()
                scores.append([score, strategy])
            # Sort by descending score
            scores = sorted(scores, key = lambda x: -1 * x[0])
            print(scores)
            topStrategies = []
            breededStrategies = []
            # Get 50 percentile of strategies
            for i in range(0, ceil(NUM_STRATEGIES / 2)):
                topStrategies.append(scores[i][1])
            print(topStrategies)
            # Breed the top strategies
            while len(breededStrategies) + len(topStrategies) < NUM_STRATEGIES:
                index1 = randint(0, len(topStrategies))
                index2 = index1
                while(index1 == index2):
                    index2 = randint(0, len(topStrategies))
                breededStrategies.append(scores[index1][1].breed(scores[index2][1]))
            print(breededStrategies)
            self.strategies.clear()
            self.strategies.extend(topStrategies)
            self.strategies.extend(breededStrategies)
            # Mutate resulting strategies
            for strategy in self.strategies:
                strategy.reset()
                strategy.mutate()

if __name__ == '__main__':
    simulation = geneticAlgorithm()
    simulation.startSimulation()

