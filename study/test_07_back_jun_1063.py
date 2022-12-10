dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

go = ["RB", "R", "RT", "B", "T", "LB", "L", "LT"]
y = ["8", "7", "6", "5", "4", "3", "2", "1"]
x = ["A", "B", "C", "D", "E", "F", "G", "H"]

# 일단 킹만
# 좌표 잡음
k, s, t = input().split()
k_point = [x.index(k[0]), y.index(k[1])]
s_point = [x.index(s[0]), y.index(s[1])]

for i in range(int(t)):
    numXY = go.index(input())

    nx = k_point[0] + dx[numXY]
    ny = k_point[1] + dy[numXY]

    if nx < 0 or ny < 0 or nx > 7 or ny > 7:
        continue
    if nx == s_point[0] and ny == s_point[1]:
        sx = s_point[0] + dx[numXY]
        sy = s_point[1] + dy[numXY]

        if sx < 0 or sy < 0 or sx > 7 or sy > 7:
            continue
        s_point[0] = sx
        s_point[1] = sy
    k_point[0] = nx
    k_point[1] = ny

k_res = x[k_point[0]] + y[k_point[1]]
s_res = x[s_point[0]] + y[s_point[1]]
print(k_res)
print(s_res)
