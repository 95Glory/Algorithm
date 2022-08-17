M = int(input())
N = int(input())
result = []

for i in range (M,N+1):
    isnot = 0
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                isnot = 1
                break

        if isnot == 0:
            result.append(i)

if len(result)>0:
    print(sum(result))
    print(min(result))
else:
    print(-1)


