A,B,C = map(int,input().split(" "))
result_A = (A+B)%C
result_B = ((A%C) + (B%C))%C
result_C = (A*B)%C
result_D = ((A%C) * (B%C))%C
print(result_A)
print(result_B)
print(result_C)
print(result_D)

