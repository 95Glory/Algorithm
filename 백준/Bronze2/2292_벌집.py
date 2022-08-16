#지나가야하는 방의 개수 1개 : 1 (1개)
#지나가야하는 방의 개수 2개 : 2, 3, 4, 5, 6, 7(6개)
#지나가야하는 방의 개수 3개 : 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19(12개)
#지나가야하는 방의 개수 4개 : 20 ~ 37(18개)
#지나가야하는 방의 개수 5개 : 38 ~ 61(24개)
n= int(input())
roomroot=1
numamount=6
num=1

if n == 1:
    print(1)
else:
    while True:
        num = num+numamount
        roomroot += 1
        if n <= num:
            print(roomroot)
            break
        numamount += 6







