import sys

input = sys.stdin.readline

dx = [0, 1, 1, -1] # 우 , 하 , 우하 , 우상
dy = [1, 0, 1, 1]

def omok():
    for x in range(19):
        for y in range(19):
            if maps[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    stone = 1

                    if not (0 <= nx < 19 and 0 <= ny < 19):
                        continue
                    while 0 <= nx < 19 and 0 <= ny < 19 and maps[x][y] == maps[nx][ny]:
                        stone += 1
                        if stone == 5:
                            if 0 <= x - dx[i] and 0 <= y - dy[i] and maps[x][y] == maps[x - dx[i]][y - dy[i]]: # 앞쪽
                                break # 같기때문에 6목 이상
                            if nx + dx[i] < 19 and ny + dy[i] < 19 and maps[nx][ny] == maps[nx + dx[i]][ny + dy[i]]: # 뒷쪽
                                break # 같기 때문에 6목 이상
                            return maps[nx][ny], x + 1 , y + 1 
                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1
maps = [list(map(int, input().split())) for _ in range(19)]

color, x, y = omok()

if not color:
    print(0)
else:
    print(color)
    print(x, y)
