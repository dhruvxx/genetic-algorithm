import numpy as np
import random

# custom imports
from probabilities import get_population_prob
from constants import MAX_DEG


def get_parents(pop, num):
    prob = get_population_prob(len(pop))
    indices = np.random.choice(np.arange(0, len(pop)), num, False, prob)
    parents = []
    for i in indices:
        parents.append(pop[i])
    return parents


def crossover(p1, p2):
    child = np.ndarray(MAX_DEG)
    for i in range(MAX_DEG):
        if random.getrandbits(1):
            child[i] = p1[i]
        else:
            child[i] = p2[i]
    return child


def get_children(parents, num):
    children = []
    i = 0
    while i in range(num):
        lol = False
        i1, i2 = np.random.choice(np.arange(0, len(parents)), 2, False)
        p1, p2 = parents[i1], parents[i2]
        child = crossover(p1, p2)
        for p in parents:
            if np.array_equal(p, child):
                lol = True
        if lol:
            print("wincest")
            continue
        else:
            children.append(child)
            i += 1
    return children
