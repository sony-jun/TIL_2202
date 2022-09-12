li_x = []
li_y = []
for _ in range(3):
    x,y = map(int,input().split())
    li_x.append(x)
    li_y.append(y)
for i in range(3):
    if li_x.count(li_x[i]) == 1:
        x4 = li_x[i]
    if li_y.count(li_y[i]) == 1:
        y4 = li_y[i]
print(x4,y4)

