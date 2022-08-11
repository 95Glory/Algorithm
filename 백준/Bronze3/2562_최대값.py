a=[]

for i in range(9):
    insert = int(input())
    a.append(insert)

result = max(a)
print(result)
print(a.index(result)+1)