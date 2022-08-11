standard = set(range(1,10001))
inputval= set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    inputval.add(i)

result = standard - inputval

for i in range(len(result)):
    a = sorted(result)
    print(a[i])