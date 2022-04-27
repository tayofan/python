from random import random


def myrandom():
    rnd = random()
    if rnd >= 0.5:
        return 0
    else:
        return 1
    
rnd = myrandom()
print("rnd",rnd)