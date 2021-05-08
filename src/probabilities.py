import numpy as np


def get_population_prob(num):
    prob = np.ndarray(num)
    for i in range(num):
        prob[i] = num - i*0.5
    prob /= np.sum(prob)
    return prob


if __name__ == "__main__":
    prob = get_population_prob(10)
    print(prob)
    print(np.sum(prob))
