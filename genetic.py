import neat
from space_invaders import *
import time

class Learner:
    def __init__(self, config_file):
        self.config = neat.Config(neat.DefaultGenome,
                                  neat.DefaultReproduction,
                                  neat.DefaultSpeciesSet, 
                                  neat.DefaultStagnation,
                                  config_file)
        self.env = Game()

    def eval_genomes(self, genomes, config):
        t0 = time.time()
        nets = []
        for genome_id, genome in genomes:
            nets.append(neat.nn.FeedForwardNetwork.create(genome, config))
        print("network creation time {0}".format(time.time() - t0))
        for (genome_id, genome), net in zip(genomes, nets):
            genome.fitness = self.env.evaluate(net)

    def run(self):
        p = neat.Population(self.config)

        # report some intermediate stats
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        p.add_reporter(neat.Checkpointer(5))

        # run for 300 generations
        winner = p.run(self.eval_genomes, 30)

        # Display the winning genome.
        print('\nBest genome:\n{!s}'.format(winner))
        self.env.render(winner)

if __name__ == '__main__':
    learner = Learner('neat.cfg')
    learner.run()
    learner.env.end_game()