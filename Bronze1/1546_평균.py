N = int(input())

score = list(map(int,input().split()))
fake_scor=[]

M = max(score)

for i in range(N):
    fake_scor.append(score[i]/M*100)

avaerge_score = sum(fake_scor)/N
print(avaerge_score)