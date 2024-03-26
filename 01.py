#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random as rd

def Dice():
    order = input("dice ") 
    count = 0
    for i in range(100):
        dice1 = np.random.randint(1,7)  #1
        dice2 = np.random.randint(1,7)  #1
        dice3 = np.random.randint(1,7)  #1

        if order:
            print("주사위를 던지자!", dice1, dice2, dice3)
            if (dice1 != dice2) or (dice1 != dice3) or (dice2 != dice3):
                print("땡!")
                count=count+1
            elif dice1 == dice2 == dice3:
                count=count+1
                print("빙고! 던진횟수: ", count)
                break
    
Dice()


# In[64]:


# if dice1 != dice2:
          #     print("땡!")
          #     count=count+1
          # elif dice1 != dice3:
          #     print("땡!")
          #     count=count+1
          # elif dice2 != dice3:
          #     print("땡!")
          #     count=count+1

