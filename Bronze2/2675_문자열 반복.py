T = int(input())

for i in range(T):
    r,S =map(str,input().split())
    R = int(r)
    for j in range(len(S)):
        print(R*S[j],end="")
    print()