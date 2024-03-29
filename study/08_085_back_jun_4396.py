dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
t = int(input())
matrix = [list(input()) for _ in range(t)]
x_matrix = [list(input()) for _ in range(t)]
num = [[0] * t for _ in range(t)]
for x in range(t):
    for y in range(t):
        cnt = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= t or ny >= t:
                continue
            if matrix[nx][ny] == "*":
                cnt += 1
        num[x][y] = cnt
resulted = [[0] * t for _ in range(t)]
# 1. x에 *이 존재할 경우!!!
# 2. x에 *이 존재하지 않을경우!!!
X_cnt = 0

for p in range(t):
    for q in range(t):
        if x_matrix[p][q] == "x" and matrix[p][q] == "*":
            X_cnt += 1


for w in range(t):
    for r in range(t):
        if x_matrix[w][r] == "x" and matrix[w][r] == "*":
            resulted[w][r] = "*"
        elif x_matrix[w][r] == "x" and matrix[w][r] == ".":
            resulted[w][r] = num[w][r]
        elif x_matrix[w][r] == "." and matrix[w][r] == ".":
            resulted[w][r] = "."
        elif x_matrix[w][r] == "." and matrix[w][r] == "*":
            if X_cnt > 0:
                resulted[w][r] = "*"
            else:
                resulted[w][r] = "."


for u in range(t):
    for b in range(t):
        print(resulted[u][b], end="")
    print()


"""
8
...**..*
......*.
....*...
........
........
.....*..
...**.*.
.....*..
xxxx....
....xxxx
xxxx....
....xxxx
xxxx....
....xxxx
xxxx....
....xxxx
"""


"""
8
...**..*
......*.
....*...
........
........
.....*..
...**.*.
.....*..
xxx.....
xxxx....
xxxx....
xxxxx...
xxxxx...
xxxxx...
xxx.....
xxxxx...
"""


""" BFS를 사용한 방식
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def bfs(a, b):
    cnt = 0
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == "*":
                    cnt += 1
    return cnt
n = int(input())
maps = [list(input().rstrip()) for _ in range(n)]
maps2 = [list(input().rstrip()) for _ in range(n)]
answer = [["."] * n for _ in range(n)]
check = False

for i in range(n):
    for j in range(n):
        if maps[i][j] == "." and maps2[i][j] == "x":
            answer[i][j] = bfs(i, j)
        if maps[i][j] == "*" and maps2[i][j] == "x":
            check = True
if check:
    for i in range(n):
        for j in range(n):
            if maps[i][j] == "*":
                answer[i][j] = "*"
for i in range(n):
    print("".join(map(str, answer[i])))
"""
