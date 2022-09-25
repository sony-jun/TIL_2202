li = []
for i in range(9):
    ki = int(input())
    li.append(ki)
chil = []
for i in range(8):
    for j in range(i+1,9):
        cnt = sum(li) - (li[i]+li[j])
        if cnt == 100:
            chil.append(li[i])
            chil.append(li[j])

li.remove(chil[0])
li.remove(chil[1])

li_so = sorted(li)
for k in li_so:
    print(k)

