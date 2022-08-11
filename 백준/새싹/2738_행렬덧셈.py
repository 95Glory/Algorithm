a,b = [],[]
m,n = map(int, input().split())

for row in range(m):
    row = list(map(int,input().split()))
    a.append(row)

for row in range(m):
    row = list(map(int,input().split()))
    b.append(row)

for q in range(m):
    for w in range(n):
        print(a[q][w]+b[q][w], end=' ')
    print()
