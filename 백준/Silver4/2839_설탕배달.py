N = int(input())
box = 0;

while N>=0:
    if N%5==0:
        box += N//5
        N = 0
        print(box)
        break
    elif N<3:
        print(-1)
        break
    else:
        N-=3
        box +=1