import math
import itertools
from uav import *

class System:
    def __init__(self, ob, alpha=0.5):
        self.ob = ob
        self.shortest_route = []
        self.shortest_distance = float('inf')
        self.distances = []
        self.alpha = alpha

        self.matrix_cost()
        self.brute_force()

    def matrix_cost(self):
        # Tạo ma trận khoảng cách
        for i in range(len(self.ob)):
            row = []
            for j in range(len(self.ob)):
                if i == j:
                    row.append(0)
                else:
                    distance = math.sqrt((self.ob[i].pos_x - self.ob[j].pos_x)**2 + (self.ob[i].pos_y - self.ob[j].pos_y)**2)
                    row.append(distance)
            self.distances.append(row)


    # Hàm tính khoảng cách đường đi
    def calculate_distance(self, route):
        cost = 0
        for i in range(len(route)):
            if i == len(route) - 1:
                cost += self.distances[route[i]][route[0]]
            else:
                cost += self.distances[route[i]][route[i+1]]
        return cost
    

    # Tìm đường đi ngắn nhất bằng phương pháp Brute force
    def brute_force(self):
        # Tạo danh sách tất cả các đường đi có thể có
        all_routes = list(itertools.permutations(range(len(self.ob))))

        # Tìm đường đi ngắn nhất trong danh sách các đường đi
        self.shortest_distance = float('inf')
        self.shortest_route = []
        for route in all_routes:
            distance = self.calculate_distance(route)
            if distance < self.shortest_distance:
                self.shortest_distance = distance
                self.shortest_route = route

        return self.shortest_route

    # Tính tổng số user
    def sum_user(self):
        user = 0
        for i in range(len(self.ob)):
            user += self.ob[i].nk

        return user

    # Tính tổng size data truyền đi
    def sum_data(self):
        data = 0
        for i in range(len(self.ob)):
            for j in range(self.ob[i].nk):
                data += self.ob[i].si[j]

        return data

    # Tính theo từng đoạn đường
    def time_move(self, v = 20.0):
        return self.shortest_distance/v
    
    # Tính thời gian đứng im thu thập dữ liệu
    def time_receive(self):
        time = 0
        for i in range(len(self.ob)):
            for j in range(self.ob[i].nk):
                time += self.ob[i].di[j]

        return time
    
    # Tính Công suất tiêu thụ trên đường đi
    def Pff_all(self):
        Pff = UAV().Pff()

        return Pff*self.time_move()
    
    # Tính công suất tiêu thụ khi truyền dữ liệu
    def Ph_all(self, time=0):
        Ph = UAV().Ph()

        if time == 0:
            return Ph*self.time_receive()
        return Ph*time
    
    # Tổng năng lượng tiêu thụ
    def P_all(self, time=0):
        Pff = self.Pff_all()
        Ph = self.Ph_all(time)

        return Pff + Ph