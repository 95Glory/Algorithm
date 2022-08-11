N, X = map(int, input().split())
a = list(map(int, input().split()))
answer = []
for i in range(N):
    if a[i] < X:
        answer.append(a[i])

for j in range(len(answer)):
    print(answer[j], end=' ')