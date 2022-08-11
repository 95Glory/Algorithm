c = int(input())
for i in range(c):
    sum = 0
    count = 0
    a = list(map(int, input().split()))
    for i in a:
        sum += i
    sum1 = sum - a[0]
    average = sum1/a[0]
    for j in a[1::]:
        if j > average:
            count += 1
    answer = count / a[0]
    print(f'{answer:.3%}')