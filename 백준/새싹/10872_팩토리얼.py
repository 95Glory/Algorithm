num = int(input())
total = 1
if num == 0:
    print(1)
elif num != 0:
    for i in range(num,0,-1):
        total = total*i
    print(total)