from strategy import Strategy
from spaceinvaders import SpaceInvaders

class geneticAlgorithm(object):
    def __init__(self):
        self.strategies = []
        for i in range(0, 50):
            self.strategies.append(Strategy())
    
    def startSimulation(self):
        scores = []
        for strategy in self.strategies:
            game = SpaceInvaders(strategy)
            score = game.main()
            scores.append(score)
        print(scores)


if __name__ == '__main__':
    simulation = geneticAlgorithm()
    simulation.startSimulation()

