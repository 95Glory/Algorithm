T = int(input())

for i in range(1,T+1):
    x, y = map(int,input().split())
    print("Case #{0}: {1} + {2} = {3}".format(i,x,y,x+y))