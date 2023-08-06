# khai báo các thông tin cần xử dụng
import random
import math
from center import *
from uav import * 
from system import *
from ga_optimizer import *   
    
if __name__ == '__main__':
    n = 9
    list_ob = []
    for i in range(n):
        c = Center()
        list_ob.append(c)

    # Get list time user 
    list_time_user = []
    for i in list_ob:
        for j in i.di:
            list_time_user.append(j)
    # print(list_time_user)
    # print()

    # print(list_ob[0].di)
    # print(list_ob[0].di[1])
    process_ga = GA(list_ob, T_deadline=10000, list_time_user=list_time_user)
    process_ga.train()
