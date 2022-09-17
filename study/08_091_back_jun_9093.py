t = int(input())
for _ in range(t):
    li = list(input().split())
    for j in li:
        print(j[::-1],end=' ')
