now_H,now_M = map(int,input().split(" "))
spend_time = int(input())
spend_hour = spend_time // 60
spend_minute = spend_time % 60
finish_H = now_H + spend_hour
finish_M = now_M + spend_minute

if finish_M >= 60:
    finish_H += 1
    finish_M -= 60
if finish_H >= 24:
    finish_H -= 24
print(finish_H,finish_M)