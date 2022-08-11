result=1

for i in range(3):
    plus = int(input())
    result *= plus

str_result = str(result)

for i in range(10):
    print(str_result.count(str(i)))