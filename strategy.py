from pygame import *
from random import randint

class Strategy(object):
    def __init__(self):
        ### 0 is left, 1 is right, 2 is space, 3 is nothing
        self.keys = []
        for i in range(0, 2000):
            self.keys.append(randint(0, 3))
        self.index = 0
    
    def next_key(self):
        ans = [False] * 323
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

    