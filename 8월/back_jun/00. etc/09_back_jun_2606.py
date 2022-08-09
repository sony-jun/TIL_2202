from pprint import pprint

n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]


bin = []
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
  
for i in range(n+1):
    for j in range(n+1):
        if graph[1][i] ==1 and graph[i][j] == 1:
            graph[1][j] = 1

        if graph[i][1] ==1 and graph[j][i] ==1:
            graph[j][1] = 1

for i in range(len(graph[1])):
    if graph[1][i] == 1:
        bin.append(i)
print(graph)

# 이렇게 하면 한번 밖에 연결된게 나오지 않는다...여러번 돌아가려면 어떻게 
# 해아하나?
