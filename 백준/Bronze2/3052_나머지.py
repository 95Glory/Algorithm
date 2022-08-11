a = []

for i in range(10):
    b = int(input())
    a.append(b%42)

result = list(set(a))
print(len(result))
