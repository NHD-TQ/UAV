# khai báo các thông tin cần xử dụng
import random
import math
from center import *
from uav import * 
from system import *
from optimizer_user import *   
    
if __name__ == '__main__':
    n = 9
    list_ob = []
    for i in range(n):
        c = Center()
        c.gen_point()

        list_ob.append(c)

    # route = System(list_ob)
    # route.imp()
    # print(route.shortest_route)
    # print(route.shortest_distance)
    # print(route.P_all())

    # print(len(list_ob[8].name_user))
    # print(list_ob[8].si)
    # print(list_ob[8].di[0])
    list_user = []
    for c in list_ob:
        list_user.append(c.name_user)
    print(list_user)
    # get population
    def init_pos(list_user):
        
        result = []

        for sublist in list_user:
            random_index = random.choice(sublist)
            selected_values = [1 if val == random_index else -1 for val in sublist]
            result.append(selected_values)

        for row in result:
            print(row, end=' ')
    init_pos(list_user)


    print(max_user(list_ob))


