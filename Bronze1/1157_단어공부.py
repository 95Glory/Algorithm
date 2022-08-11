text = input().upper()
detext = []
indexnum=[]

for i in text:
    if i not in detext:
        detext.append(i)

for i in range(len(detext)):
    index = text.count(detext[i])
    indexnum.append(index)

if indexnum.count(max(indexnum)) > 1:
    print("?")
else:
    max_index = indexnum.index(max(indexnum))
    print(detext[max_index])