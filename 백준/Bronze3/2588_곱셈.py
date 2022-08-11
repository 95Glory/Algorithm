num = int(input())
num2 = input()

for i in range(len(num2)-1,-1,-1):
    qq = int(num2[i])
    print(num * qq)
print(num * int(num2))