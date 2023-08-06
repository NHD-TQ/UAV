class fitness:
    def __init__(self, P_all, N_max, T_min, S_max, alpha = 10000, beta = 100, grama = 100):
        self.P_all = P_all
        self.N_max = N_max
        self.T_min = T_min
        self.S_max = S_max
        self.alpha = alpha
        self.beta = beta
        self.grama = grama

    def fitness_all(self):
        fitness = self.P_all - self.alpha*self.N_max + self.beta*self.T_min - self.grama*self.S_max
        return fitness
    
    def fitness_noP(self):
        fitness = self.alpha*self.N_max + self.beta*self.T_min - self.grama*self.S_max
        return fitness
    
    def fitness_P1(self):
        fitness = self.P_all - self.alpha*self.N_max
        return fitness
    
    def fitness_P2(self):
        fitness = self.P_all + self.beta*self.T_min
        return fitness
    
    def fitness_P3(self):
        fitness = self.P_all - self.grama*self.S_max
        return fitness