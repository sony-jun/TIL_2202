li = []
for i in range(1, 6):
    a = input()
    if a.count("FBI") >= 1:
        li.append(i)
if li == []:
    print("HE GOT AWAY!")
else:
    print(*li)
