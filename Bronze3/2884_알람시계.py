set_time = list(map(int,input().split(" ")))

if set_time[1] >= 45:
    print(set_time[0],set_time[1]-45,sep=" ")
elif set_time[0] != 0 and set_time[1] < 45:
    minus = set_time[1]-45
    print(set_time[0]-1,60+minus)
elif set_time[0] == 0 and set_time[1] < 45:
    minus = set_time[1]-45
    print(23,60+minus)

