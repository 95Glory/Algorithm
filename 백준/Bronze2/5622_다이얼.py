number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
count = 0

for i in number :
    for j in i:
        for x in word :
            if j == x :  #
                count += number.index(i) +3
print(count)

