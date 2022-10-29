li_1 = []
li_2 = []
for i in range(10):
    li_1.append(int(input()))
for j in range(10):
    li_2.append(int(input()))
li_1.sort()
li_2.sort()
print(sum(li_1[7:]), sum(li_2[7:]))
