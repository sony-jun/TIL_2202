a, b = map(int, input().split())
li = []
for i in range(1, a + 1):
    li.append(i)
li_2 = []
while True:
    if li == []:
        break
    cnt = b
    li_2.append(li[b - 1])
    li.pop(li[b - 1])
