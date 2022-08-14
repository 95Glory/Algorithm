# A,B,V = map(int,input().split())
# day = 0
# while True:
#     if A >= V:
#         day +=1
#         print(day)
#         break
#     V -= (A-B)
#     day += 1
A,B,V = map(int, input().split())

if (V-B) % (A-B) == 0 :
    print((V-B) // (A-B))
else :
    print(((V-B) // (A-B)) +1)

