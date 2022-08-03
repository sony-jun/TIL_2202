import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
x = 0
y = 0
for i in range(n):
    if 'X' not in matrix[i]:
        x += 1
for j in range(m):
    
    if 'X' not in [matrix[i][j] for i in range(n)]:
        y += 1

print(min(x,y))