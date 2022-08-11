x,y,z = map(int,input().split())

maxint=max([x,y,z])

if x == y == z:
    print(10000+x*1000)
elif x == y != z:
    print(1000+x*100)
elif x == z != y:
    print(1000+x*100)
elif y == z != x:
    print(1000+y*100)
else:
    print(maxint*100)