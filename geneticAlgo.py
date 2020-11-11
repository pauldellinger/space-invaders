from strategy import Strategy
from random import randint
from math import ceil
from stats import *
import gym
import numpy as np
from datetime import datetime
import os
import pickle

class geneticAlgorithm(object):
    def __init__(self, 
                 NUM_GENERATIONS=50,
                 NUM_STRATEGIES=20,
                 SELECTIVITY = 0.25,
                 EPISODES=3, # TODO: some statistics on what's a good value
                 GAME='SpaceInvaders-v0',
                 MUTATION_RATE=0.01
                 ):
        self.NUM_GENERATIONS = NUM_GENERATIONS
        self.NUM_STRATEGIES = NUM_STRATEGIES
        self.SELECTIVITY = SELECTIVITY
        self.EPISODES = EPISODES
        self.MUTATION_RATE = MUTATION_RATE
        self.strategies = []
        for i in range(0, NUM_STRATEGIES):
            self.strategies.append(Strategy(MUTATE_PROBABILITY=MUTATION_RATE))
        self.env = gym.make(GAME)
        self.env.reset()
        self.start_time = datetime.now()
        self.folder = os.path.join('strategies', self.start_time.strftime("%Y%m%d-%H%M%S"))
        os.mkdir(self.folder)
    
    def evaluateScore(self, strategy):
        scores = []
        for _ in range(self.EPISODES):

            observation = np.array(self.env.reset())
            score = 0
            while True:
                observation, reward, done, info = self.env.step(strategy.calculateMove(observation))
                score += reward
                if(done):
                    scores.append(score)
                    break
        return (sum(scores)/len(scores))
    
    def startSimulation(self):
        results = []
        for i in range(1, self.NUM_GENERATIONS):
            print("GENERATION: " + str(i))
            scores = []
            sumScores = 0
            for strategy in self.strategies:
                score = self.evaluateScore(strategy)
                sumScores += score
                scores.append([score, strategy])
            # Sort by descending score
            results.append(scores)
            scores = sorted(scores, key = lambda x: -1 * x[0])
            print("Max: " + str(scores[0][0]))
            print("Average: " + str(sumScores / self.NUM_STRATEGIES))
            topStrategies = []
            breededStrategies = []
            # Get 75 percentile of strategies
            for i in range(0, ceil(self.NUM_STRATEGIES * self.SELECTIVITY)):
                topStrategies.append(scores[i][1])
            # Breed the top strategies
            # Don't want to lose our top strategies...so only mutate breeded ones
            while len(breededStrategies) + len(topStrategies) < self.NUM_STRATEGIES:
                index1 = randint(0, len(topStrategies))
                index2 = index1
                while(index1 == index2):
                    index2 = randint(0, len(topStrategies))
                breededStrategies.append(scores[index1][1].breed(scores[index2][1]))
            self.strategies.clear()
            self.strategies.extend(topStrategies)
            for strategy in breededStrategies:
                strategy.mutate()
            self.strategies.extend(breededStrategies)
            
        print("Simulation time: ", datetime.now() - self.start_time, "\n")
        
        return results
    
    # Run many sims.
    def run_simulations_with_params(self, paramList, variable="Selectivity"):
        # Init.
        allSimStats = []

        # Each sim.
        for specs in paramList:
            self.SELECTIVITY = specs[1]                     # Set Selectivity.
            self.strategies = []                            # Clear.
            for i in range(0, self.NUM_STRATEGIES):
                s = Strategy(MUTATE_PROBABILITY=specs[0])   # Set Mutability.
                self.strategies.append(s)
            
            # Run.
            results = self.startSimulation()

            # Save intermediate results.
            path = os.path.join(self.folder, str(specs))
            os.mkdir(path)
            sim_results_path = os.path.join(path, str(specs)+  '-sim-results' )
            os.mkdir(sim_results_path)
            self.export_results(results, sim_results_path)

            # Stats.
            stats = fetch_simulation_stats(results)
            
            # Append.
            print(stats)
            allSimStats.append(stats)
        
        # Build.
        varLst = [i[variable=="Selectivity"] for i in paramList]
        legendLabels = list(map(lambda x: variable + "=" + str(x), varLst))
        for stat in ('avg', 'max'):
            Ys = []
            Xs = []
            for i in range(len(allSimStats)):
                Ys.append([])
                for j in range(len(allSimStats[i])):
                    Ys[i].append(allSimStats[i][j][stat])
                Xs.append(range(len(allSimStats[i])))
            d = {
                
                "Xs": Xs,
                "Ys":Ys,
                "title" : variable + "'s effect on " + stat + "score",
                "xLabel" : "Generation",
                "yLabel" : stat + "Score",
                "n" : len(allSimStats),
                "legendLabels" : legendLabels
            }
            plt = make_plot(d['title'], d['xLabel'], d['yLabel'])
            compiled_results = list(zip(d['Xs'], d['Ys'], d['legendLabels']))
            add_lines(plt, compiled_results)
            save_plot(plt, stat + variable + self.start_time.strftime("%Y%m%d-%H%M%S"))
            
        
        # Ret.
        return allSimStats
    
    def export_results(self, results, path):
        now = datetime.now().strftime("%Y%m%d-%H%M%S")
        pickle.dump(self, open(os.path.join(path, now + '-results.p'), "wb"))
        for gen, generation in enumerate(results):
            gen = str(gen)
            gen_path = os.path.join(path, gen)
            os.mkdir(gen_path)
            for (score, strat) in generation:
                score = str(int(score))

                strat.export(score, gen_path)
                """ 
                Can load results like this:
                loaded = Strategy.load_strategy(path + "/" + gen + '-' + score + '.p')
                """


if __name__ == '__main__':
    simulation = geneticAlgorithm(10, 2)

    ####################
    # Single Mode.
    ####################
    # results = simulation.startSimulation()
    

    ####################
    #### Many Mode.
    ####################
    paramList = [
        [0.01, 0.05],
        [0.01, 0.10],
        # [0.01, 0.15],
        # [0.01, 0.20],
        # [0.01, 0.25],
        # [0.01, 0.30],
        # [0.01, 0.35],
        # [0.01, 0.40],
        # [0.01, 0.45],
        # [0.01, 0.5]
    ]
    simulation.run_simulations_with_params(paramList, variable="Selectivity")
    

    



    
