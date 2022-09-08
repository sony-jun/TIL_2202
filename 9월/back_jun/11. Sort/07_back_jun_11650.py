n = int(input())
li = []
for i in range(n):
    [a,b] = map(int,input().split())
    li.append([a,b])
so_li = sorted(li)
for j in range(n):
    print(so_li[j][0],so_li[j][1])

