def max_user(list_ob, T_deadLine=30):
    list_selected_user = []
    for center in list_ob:
        user_time = []
        user_selected = []
        user_time_source = []
        for i in range(len(center.name_user)):
            user_time.append(center.di[i])
            user_time_source.append(center.di[i])
        # Sắp xếp thời gian user để chọn theo T-deadline
        user_time.sort()
        # Cộng dồn Time user cho đến khi lớn hươn T_deadline thì dừng 
        sum_time = 0
        sl = []
        for i in range(len(user_time)):
            sum_time += user_time[i]
            if sum_time <= T_deadLine:
                sl.append(user_time[i])
            else:
                break
        for i in user_time:
            for j in range(len(user_time_source)):
                if user_time_source[j] == i:
                    user_selected.append(j)
        list_selected_user.append(user_selected)   

    return list_selected_user    