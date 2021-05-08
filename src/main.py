import numpy as np
import time

# custom imports
from client import get_errors, get_overfit_vector
from constants import POPULATION_SIZE, NUM_GEN
from population import get_initial_population, get_population_error, update_pop_log, new_pop_log, get_mutated_pop
from parents import get_parents, get_children

# generate initial population

pop = get_initial_population(POPULATION_SIZE)

# errors, total_err = get_population_error(pop, True)
timestr = time.strftime("%d-%m-%H:%M:%S")
f = open('./final_logs/' + timestr + '_generations.txt', 'a')

for g in range(250, 501):

    # initial
    new_pop_log(pop, f, 'Initial Population', g)

    # selection of parents
    train_err, val_err, total_err = get_population_error(pop, True, g)

    sorted_pop = [x for _, x in sorted(
        zip(total_err, pop), key=lambda pair: pair[0])]

    parents = get_parents(sorted_pop, 6)

    new_pop_log(parents, f, 'After Selection')

    # cross-over (=> children)

    children = get_children(parents, 8)

    new_pop = np.concatenate((sorted_pop[:2], children))
    print(np.shape(new_pop))  # debug
    new_pop_log(new_pop, f, 'After Cross-over')

    # mutation (=> new generation)

    pop = get_mutated_pop(new_pop)
    new_pop_log(pop, f, 'After Mutation')

f.close()
update_pop_log(pop)
# get_population_error(pop, True)
