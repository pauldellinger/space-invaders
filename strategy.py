from pygame import *
from random import randint

MUTATE_PROBABILITY = 5 # (out of 100)
NUM_KEYS = 4000
KEYBOARD_LENGTH = 323


class Strategy(object):
    def __init__(self, keys = None):
        ### 0 is left, 1 is right, 2 is space, 3 is nothing
        if(keys is None):
            self.keys = []
            for i in range(0, NUM_KEYS):
                self.keys.append(randint(0, 3))
        else:
            self.keys = keys
        self.index = 0
    
    def reset(self):
        self.index = 0
    
    def next_key(self):
        ans = [False] * KEYBOARD_LENGTH
        if(self.index == len(self.keys)):
            ### Do nothing
            return tuple(ans)
        
        temp = self.keys[self.index]
        self.index += 1

        if(temp == 0):
            self.index += 1
            ans[K_LEFT] = True
            return tuple(ans)
        elif(temp == 1):
            ans[K_RIGHT] = True
            return tuple(ans)
        elif(temp == 2):
            ans[K_SPACE] = True
            return tuple(ans)
        else:
            return tuple(ans)
    
    def mutate(self):
        for i in range(0, len(self.keys)):
            if(randint(1, 100) <= MUTATE_PROBABILITY):
                old = self.keys[i]
                while(self.keys[i] == old):
                    self.keys[i] = randint(0, 3)
    
    def breed(self, other):
        newKeys = []
        for i in range(0, NUM_KEYS):
            if(randint(1, 2) == 1):
                newKeys.append(self.keys[i])
            else:
                newKeys.append(other.keys[i])
        return Strategy(keys = newKeys)

    