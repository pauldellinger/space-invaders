from strategy import Strategy
from spaceinvaders import SpaceInvaders
from random import randint
from math import ceil

# Number of generations to run
NUM_GENERATIONS = 10

# Number of strategies to test in each generation
NUM_STRATEGIES = 20

class geneticAlgorithm(object):
    def __init__(self):
        self.strategies = []
        # For the first generation, initialize with random strategies
        for i in range(0, NUM_STRATEGIES):
            self.strategies.append(Strategy())
    
    def startSimulation(self):
        # Run each generation
        for i in range(0, NUM_GENERATIONS):
            print("GENERATION: " + str(i))
            scores = []
            sumScores = 0
            # Evaluate the score for all strategies
            for strategy in self.strategies:
                game = SpaceInvaders(strategy)
                score = game.main()
                sumScores += score
                scores.append([score, strategy])
            # Sort by descending score
            scores = sorted(scores, key = lambda x: -1 * x[0])
            print("Max: " + str(scores[0][0]))
            print("Average: " + str(sumScores / NUM_STRATEGIES))
            topStrategies = []
            breededStrategies = []
            # Get top 50 percentile of strategies
            for i in range(0, ceil(NUM_STRATEGIES / 2)):
                topStrategies.append(scores[i][1])
            # Breed the top strategies
            while len(breededStrategies) + len(topStrategies) < NUM_STRATEGIES:
                index1 = randint(0, len(topStrategies))
                index2 = index1
                while(index1 == index2):
                    index2 = randint(0, len(topStrategies))
                breededStrategies.append(scores[index1][1].breed(scores[index2][1]))
            # Strategies for next generation are the top strategies and breeded strategies
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

