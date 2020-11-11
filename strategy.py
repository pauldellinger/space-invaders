from pygame import *
from random import randint
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle
import os.path

MUTATE_PROBABILITY = 1 # (out of 100)
NUM_PIXELS = 7896
NUM_MOVES = 6

class Strategy(object):
    def __init__(self, 
                 w0 = None, 
                 b0 = None,
                 MUTATE_PROBABILITY=0.01,
                 MUTATION_FACTOR=2
                 ):
        # Initialize weights and bias for layer one (normal distribution in [-1, 1))
        if(w0 is None and b0 is None):
            self.w0 = 2 * np.random.rand(NUM_PIXELS, NUM_MOVES) - 1
            self.b0 = 2 * np.random.rand(NUM_MOVES) - 1
        else: 
            self.w0 = w0
            self.b0 = b0
        self.MUTATE_PROBABILITY = MUTATE_PROBABILITY
        self.MUTATION_FACTOR = MUTATION_FACTOR
    
    # Convert image to black and white and reduce size to make computation faster
    def preprocessImage(self, pixelInput):
        observation = cv2.cvtColor(cv2.resize(pixelInput, (84, 110)), cv2.COLOR_BGR2GRAY)
        observation = observation[16:110,:]
        ret, observation = cv2.threshold(observation,1,255,cv2.THRESH_BINARY)
        observation = observation.flatten()
        return np.where(observation == 0, observation, 1)

    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-x))
    
    def calculateMove(self, pixelInput):
        pixelInput = self.preprocessImage(pixelInput)
        output = pixelInput.dot(self.w0) + self.b0
        output = self.sigmoid(output)
        return np.argmax(output)

    def mutate(self):
        for i in range(0, NUM_PIXELS):
            for j in range(0, NUM_MOVES):
                if(np.random.rand() <= self.MUTATE_PROBABILITY):
                    self.w0[i][j] += randint(-self.MUTATION_FACTOR, self.MUTATION_FACTOR)
        for i in range(0, NUM_MOVES):
            if(np.random.rand()<= self.MUTATE_PROBABILITY):
                self.b0[i] += randint(-self.MUTATION_FACTOR, self.MUTATION_FACTOR)
    
    def breed(self, other):
        newWeights = np.empty([NUM_PIXELS, NUM_MOVES])
        newBias = np.empty([NUM_MOVES])
        for i in range(0, NUM_PIXELS):
            for j in range(0, NUM_MOVES):
                if(randint(1, 2) == 1):
                    newWeights[i][j] = self.w0[i][j]
                else:
                    newWeights[i][j] = other.w0[i][j]
                # newWeights[i][j] = (self.w0[i][j] + other.w0[i][j]) / 2.0
        for i in range(0, NUM_MOVES):
            if(randint(1, 2) == 1):
                newBias[i] = self.b0[i]
            else:
                newBias[i] = other.b0[i]
        # newBias = (self.b0 + other.b0) / 2.0
        return Strategy(newWeights, newBias)

    def export(self, score, gen, start):
        score, gen = str(score), str(gen)
        pickle.dump(self, open(os.path.join("strategies", start, gen + '-' + score + '.p'), "wb"))
    

    @staticmethod
    def load_strategy(path):
        return pickle.load(open(path, "rb"))

