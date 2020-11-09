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
while True:
    # Render.
    env.render()

    # Delay.
    if i == 0:
        time.sleep(5)
    else:
        time.sleep(0.025)

    # Listen.
    try:
        if keyboard.is_pressed('space'):  # Shoot.
            env.step(1)
            continue
        elif keyboard.is_pressed('right'):  # Right.
            env.step(2)
            continue
        elif keyboard.is_pressed('left'):  # Left.
            env.step(3)
            continue
        elif keyboard.is_pressed('right') and keyboard.is_pressed('space'):  # Right + Shoot.
            env.step(4)
            continue
        elif keyboard.is_pressed('left') and keyboard.is_pressed('space'):  # Left + Shoot.
            env.step(5)
            continue
        
        # Default.
        env.step(0)
        
        # Increment.
        i+=1
    except:         # Sanity.
        continue
    
