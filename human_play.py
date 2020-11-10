# Game.
import gym
import numpy as np

# User.
import keyboard
import time

# Init.
env = gym.make('SpaceInvaders-v0')
env.reset()

# Launch.
env.render()
i = 0
score = 0
done = False
while True:
    # Render.
    env.render()
    if done:
        print("score: ", score)
        break
    # Delay.
    if i == 0:
        time.sleep(5)
    else:
        time.sleep(0.025)

    # Listen.
    try:
        if keyboard.is_pressed('space'):  # Shoot.
            observation, reward, done, info = env.step(1)
            score += reward
            continue
        elif keyboard.is_pressed('right'):  # Right.
            observation, reward, done, info = env.step(2)
            score += reward
            continue
        elif keyboard.is_pressed('left'):  # Left.
            observation, reward, done, info = env.step(3)
            score += reward
            continue
        elif keyboard.is_pressed('right') and keyboard.is_pressed('space'):  # Right + Shoot.
            observation, reward, done, info = env.step(4)
            score += reward
            continue
        elif keyboard.is_pressed('left') and keyboard.is_pressed('space'):  # Left + Shoot.
            observation, reward, done, info = env.step(5)
            score += reward
            continue
        
        # Default.
        observation, reward, done, info = env.step(0)
        score += reward 
        # Increment.
        i+=1
    except:         # Sanity.
        continue
    
