total = int(input())
buycount = int(input())
totalprice=0

for i in range(buycount):
    price,count = map(int,input().split())
    totalprice += price*count

if totalprice==total:
    print("Yes")
else:
    print("No")