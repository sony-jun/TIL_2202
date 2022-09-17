# pypy로 하지 않으면 통과하지 않는다

n,m = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

for w in range(t):
    cnt = 0
    i,j,x,y = map(int,input().split())
    for e in range(i-1,x):
        for r in range(j-1,y):
            cnt += matrix[e][r]
    print(cnt)
