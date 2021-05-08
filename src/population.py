import numpy as np
import time

# custom imports
from client import get_errors
from constants import *


def get_random_population(num):
    pop = []
    for _ in range(num):
        member = np.random.uniform(-50, 50, MAX_DEG)
        member = np.multiply(member, MAGN_VECTOR)
        pop.append(member.tolist())
    return pop


def get_initial_population(num):
    try:
        from sample import pop
    except:
        pop = get_random_population(num)
    return np.array(pop)


def get_population_error(pop, log=False, gen=0):
    train_err, val_err, total_err = [], [], []
    for p in pop:
        err = get_errors(list(p))  # size=2
        train_err.append(err[0])  # size=1
        val_err.append(err[1])
        total_err.append(1*err[0]+1*err[1])
    if log:
        timestr = time.strftime("%d-%m-%H.%M.%S")
        f = open('./error_logs/' + timestr + '_errors.txt', 'w')
        string1 = 'train_err =' + str(train_err)
        string2 = 'val_err =' + str(val_err)
        string3 = 'total_err =' + str(total_err)
        f.writelines([string1, '\n', string2, '\n',
                      string3, '\n\n Generation=', str(gen)])
        f.close()
    return train_err, val_err, total_err  # 2xN, 1xN


def mutation(member, prob, pc):
    mem = member
    for i in range(len(mem)):
        if np.random.random_sample() <= prob:
            if mem[i]:
                factor = np.random.uniform(1 - pc, 1 + pc)
                while abs(factor - 1) < 0.05:
                    factor = np.random.uniform(1 - pc, 1 + pc)
                mem[i] *= factor
            else:
                factor = np.random.uniform(-50, 50)
                while abs(factor) < 5:
                    factor = np.random.uniform(-50, 50)
                mem[i] += factor*1e-23
    return mem


def get_mutated_pop(pop, prob=MUTATION_PROB, pc=MUTATION_FACTOR):
    mut_pop = pop
    for m in mut_pop:
        m = mutation(m, prob, pc)
    return mut_pop


def update_pop_log(pop):
    timestr = time.strftime("%d-%m-%H.%M.%S")
    f = open("sample.py", 'w')
    ftxt = open('./sample_logs/' + timestr + '_population.txt', 'w')
    string = 'pop = ' + str(pop.tolist())
    #string = 'pop = ' + str(list(pop))
    f.write(string)
    ftxt.write(str(np.array(pop)))
    f.close()
    ftxt.close()


def new_pop_log(pop, file, step, gen=None):
    if (gen is not None):
        file.write('''------------------------
        GENERATION '''+str(gen) + '\n')
    file.write('\n'+step+'\n')
    for p in pop:
        file.write(str(p) + '\n')


if __name__ == "__main__":
    pop = get_random_population(POPULATION_SIZE)
    update_pop_log(pop)
