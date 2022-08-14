N = int(input())
count = N
group = ''
for i in range(N):
    group = input()
    for j in range(len(group)-1):
        if group[j] == group[j+1]:
            pass
        elif group[j] in group[j+1:]:
            count -= 1
            break
print(count)
