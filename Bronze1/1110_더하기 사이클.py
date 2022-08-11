num = int(input())
n = num
count = 0
while True:
    # num = 68
    # 6 + 8 = 14
    a = n//10 #6
    b = n%10  #8
    c = (a+b)%10 #4
    n = int(str(b)+str(c))
    count += 1
    if num == n:
        print(count)
        break