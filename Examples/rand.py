'''
Using random number generators.
To be able to reproduce your results (bugs, random algorithm solutions, etc.),
you need to set the seed of the random generators that you are using.

@author: Vassilissa Lehoux
'''


import numpy as np
import random


def set_seed_random(seed: int):
    random.seed(seed)


def set_seed_numpy(seed: int):
    np.random.seed(seed)
    

def random_integer(min_val: int, max_val: int):
    """
    Returns a random integer drawn uniformly from a range
    """
    return random.randint(min_val, max_val)
    

def random_float():
    """
    Returns a random real number between 0 and 1
    """
    return random.random()


def change_order(mylist):
    """
    Shuffles the elements of the list
    """
    return random.shuffle(mylist)


if __name__ == '__main__':
    set_seed_random(20)
    print("random int between 0 and 10", random_integer(0, 10))
    print("random int between 5 and 10", random_integer(5, 10))
    print("random nb between 0 and 1", random_float())
    mylist = [val for val in range(10)]
    change_order(mylist)
    print("shuffling list", mylist)
