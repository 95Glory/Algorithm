full_num = list(range(1, 31))
insert_num = list(range(28))
i = 0
while i < 28:
    insert_num[i] = int(input())
    i += 1

for i in full_num :
    if i not in insert_num:
        print(i)
