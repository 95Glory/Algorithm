import math
T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
    row = math.ceil(N/H)
    if N%H == 0:
        floor = H
    else:
        floor = N%H

    print(floor,'%02d'%row,sep='')


