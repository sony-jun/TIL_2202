import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    [a,b] = map(int,input().split())
    li.append([b,a])
so_li = sorted(li)
for j in range(n):
    print(so_li[j][1],so_li[j][0])

