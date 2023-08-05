import random 
import pandas as pd
import numpy as np 

def get_fitness(individual):
    "......"
    return

def crossover(individual_a, individual_b):
    crossing_point = random.randint(0, 99)
    offspring_a = individual_a[0:crossing_point] + individual_b[crossing_point:100]
    offspring_b = individual_b[0:crossing_point] + individual_a[crossing_point:100]
    return offspring_a, offspring_b

def tournament(current_population):
    index = sorted(random.sample(range(0, 20), 5))
    tournament_members  = [current_population[i] for i in index]
    total_fitness = sum([individual[1] for individual in tournament_members])
    probabilities = [individual[1] / total_fitness for individual in tournament_members]
    index_a, index_b = np.random.choice(5, size=2, p=probabilities)
    return crossover(tournament_members[index_a][0], tournament_members[index_b][0])

def mutation(individual):
    mutation_point = random.randint(0, 99)
    if(individual[mutation_point]):
        individual[mutation_point] = 0
    else:
        individual[mutation_point] = 1

def build_next_generation(current_population, mutation_rate):
    next_generation = []
    next_generation.append(current_population[0][0]) # elitism
    next_generation.append(current_population[random.randint(1,19)][0]) # randomness

    for i in range(9): # tournaments
        offspring_a, offspring_b = tournament(current_population)
        next_generation.append(offspring_a)
        next_generation.append(offspring_b)

    for individual in next_generation: # mutation
        if(random.randint(1,mutation_rate) == 1):
            mutation(individual)
    return next_generation

