import gym
import numpy as np
from gym_wrappers import MainGymWrapper
class Game:
    def __init__(self, game='SpaceInvaders-v0', max_iter=50000):
        self.env = MainGymWrapper.wrap(gym.make(game))
        self.max_iter = max_iter

    def evaluate(self, learner):
        if not self.validate(learner):
            return 0
       	done, score, iter = False, 0, 0
        observation = np.array(self.env.reset())
        while not done and iter < self.max_iter:

            output = learner.activate(observation.flatten())
            action = np.argmax(output)
            observation, reward, done, info = self.env.step(action)
            observation = np.array(observation)
            score += reward
            iter += 1
        self.env.reset()
        return score

    def render(self, learner):
        # like evaluate, but actually show the pop up

        if not self.validate(learner):
            return 0
       	done, score, iter = False, 0, 0
        observation = np.array(self.env.reset())
        while not done and iter < self.max_iter:
            self.env.render()
            output = learner.activate(observation.flatten())
            action = np.argmax(output)
            observation, reward, done, info = self.env.step(action)
            observation = np.array(observation)
            score += reward
            iter += 1
        self.env.reset()
        print("Score: ", score)

    def get_actions(self):
        return self.env.action_space

    def get_input(self):
        return self.env.observation_space

    def end_game(self):
        self.env.close()

    def validate(self, learner):
        # todo: invalidate if it doesn't do anything for super long
        return True
