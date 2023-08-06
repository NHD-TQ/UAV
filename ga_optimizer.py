import random
import pandas as pd
import numpy as np
from numpy.random import rand
from system import *
from fitness import *


class GA():
    def __init__(self, list_ob, T_deadline, list_time_user, n_population = 20, n_gen = 20, crossover_rate = 0.8, mutation_rate = 0.2, thres = 0.5, n_up = 20):
        self.list_ob = list_ob
        self.T_deadline = T_deadline
        self.list_time_user = list_time_user
        self.n_population = n_population
        self.n_gen = n_gen
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.thres = thres
        self.n_up = n_up

        self.setting = System(self.list_ob)
        self.num_user = self.setting.sum_user()
        self.population = self.init_position()
        # self.population = self.binary_conversion(self.population)

    def set_polulation(self, population):
        self.population = population

    #Xay dung population
    def init_position(self):
        X = []
        
            
        for _ in range(self.n_population):
            while True:
                total_time_user = 0
            # list_user = [0, 1], [0, 1, 2], [...]
                list_user = [[i for i in range(self.list_ob[k].nk)] for k in range(len(self.list_ob))]
                result = []
                index_center = 0
                for sublist in list_user:
                    num_selected = random.randint(1, len(sublist)) 
                    selected_indices = random.sample(range(len(sublist)), num_selected) 
                    selected_values = [1 if i in selected_indices else 0 for i in range(len(sublist))]
                    # check Time_deadline
                    for i in range(len(selected_values)):
                        if selected_values[i] == 1:
                            self.list_ob[index_center].di[i]
                            total_time_user += self.list_ob[index_center].di[i]
                        else:
                            continue

                    index_center += 1
                    result.append(selected_values)
                if total_time_user <= self.T_deadline:
                    result = [item for sublist in result for item in sublist if sublist]
                    X.append(result)
                    break
                else:
                    continue  
                
        return X


    #Chuyen doi population thanh ma tran nhi phan
    def binary_conversion(self, X):
        N = self.n_population
        dim = self.setting.sum_user()
        thres = self.thres

        Xbin = np.zeros([N, dim], dtype='int')
        for i in range(N):
            for d in range(dim):
                if X[i,d] > thres:
                    Xbin[i,d] = 1
                else:
                    Xbin[i,d] = 0
        
        return Xbin
    
    # Lai ghép các cá thể với nhau
    def crossover(self, individual_a, individual_b):
        # check time user
     
        while True:
            total_a = 0
            total_b = 0
            
         
            dim = self.setting.sum_user()
            crossing_point = random.randint(0, dim-1)

            offspring_a = individual_a[0:crossing_point] + individual_b[crossing_point:dim]
            offspring_b = individual_b[0:crossing_point] + individual_a[crossing_point:dim]
            # a
            for i in range(len(offspring_a)):
                if offspring_a[i] == 1:
                    total_a += self.list_time_user[i]
            # b
            for i in range(len(offspring_b)):
                if offspring_b[i] == 1:
                    total_b += self.list_time_user[i]    
            if total_a <= self.T_deadline and total_b <= self.T_deadline:
                break
        # print(offspring_b)
        return offspring_a, offspring_b
    
    # Đột biến cá thể
    def mutation(self, individual):
        
        while True:
            total_time = 0
            dim = self.setting.sum_user()
            mutation_point = random.randint(0, dim-1)
       

            if(individual[mutation_point]):
                individual[mutation_point] = 0
            else:
                individual[mutation_point] = 1
            
            # check
            for i in range(len(individual)):
                if individual[i] == 1:
                    total_time += self.list_time_user[i]  
            if total_time <= self.T_deadline:
                break

        return individual

    #Tinh toan fitness
    def caculate(self):
        cost = {}
        new_population = []
        N_max = 0
        P_all = 0
        T_min = 0
        S_max = 0
        sav_cost = 0
        for i in range(self.n_population):
            system = System(self.list_ob)
            dem_user, N_max, P_all, T_min, S_max = 0, 0, 0, 0, 0
            N_max = sum(list(self.population[i]))

            # Tổng time, và data_size của tất cả user trên tất cả user 
            for j in range(len(self.list_ob)):
                for k in range(self.list_ob[j].nk):
                    T_min += self.list_ob[j].di[k]*self.population[i][dem_user]
                    S_max += self.list_ob[j].si[k]*self.population[i][dem_user]
                    dem_user += 1

            P_all = system.P_all(T_min)
            fit = fitness(P_all, N_max, T_min, S_max).fitness_all()
            cost[sav_cost] = fit
            sav_cost += 1
        cost = dict(sorted(cost.items(), key=lambda x: x[1]))
        
        new_population = [self.population[i] for i in list(cost.keys())[0:self.n_up]]
        error = [i for i in list(cost.values())[0:self.n_up]]
        return new_population, error

    # Train
    def train(self):
        population = []     #Quan the sau khi chay GA
        error = {}          #Thu tu va cost cua cac ca the GA
        the_best = []
        error_best = 100000000000
        for i in range(self.n_gen):
            print("gen " + str(i + 1) + ":")
            population, error = self.caculate()
            new_population = []
            #Crossover & mutation
            for i in range(self.n_population//2):
                cross_rate = rand()
                # vi tri ngau nhien trong quan the moi gom 20 phan tu
                individual_a_rate = random.randint(0, self.n_up-1)
                individual_a = population[individual_a_rate]

                individual_b_rate = random.randint(0, self.n_up-1)
                individual_b = population[individual_b_rate]

                #cross
                if cross_rate <= self.crossover_rate:
                    individual_a, individual_b = self.crossover(individual_a, individual_b)
                
                #Mutation
                mutation_rate = rand()
                if mutation_rate <= self.mutation_rate:
                    individual_a = self.mutation(individual_a)

                mutation_rate = rand()
                if mutation_rate <= self.mutation_rate:
                    individual_b = self.mutation(individual_b)

                new_population.append(individual_a)
                new_population.append(individual_b)

            self.set_polulation(new_population)
            print("Error: ", error[0])
            print("Population ", population[0])

            if error[0] < error_best:
                the_best = population[0]
            

        population, error = self.caculate()
        if error[0] < error_best:
            the_best = population[0]

        print("Error best: ", error[0])
        print("Population best", population[0])
        return the_best, error_best



        

