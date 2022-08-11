N = int(input())
A = list(map(int, input().split()))
V = int(input())
count = 0
for i in range(N):
    if A[i] == V:
        count += 1
print(count)