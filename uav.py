# khai báo các thông tin cần xử dụng 
import random
import math

class UAV:
    def __init__(self, m = 5, g = 9.8, p = 1.225, C_ds = 0.25, k0 = 570, v_t = 200, v = 20, A_d = 0.5):
        self.m = m
        self.g = g
        self.p = p
        self.C_ds = C_ds
        self.k0 = k0
        self.v_t = v_t
        self.v = v
        self.A_d = A_d

    
    def Pff(self):
        v_ind = math.sqrt((-self.v*self.v + math.sqrt(self.v**4 + ((self.m*self.g)/(self.p*self.A_d)**2)))/2)
        return self.m*self.g*v_ind + 1/2*self.p*(self.v**3)*self.C_ds + self.k0*(1 + 3*((self.v*self.v)/(self.v_t*self.v_t)))

    def Ph(self):
        return self.k0 + math.sqrt((self.m*self.g)**3/(2*self.p*self.A_d))