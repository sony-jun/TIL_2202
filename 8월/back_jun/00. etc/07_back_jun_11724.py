
import sys

input = sys.stdin.readline

n,m = map(int,input().split())


graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

cnt = 0
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
                
for j in range(1,n+1):
    if not visited[j]:
        dfs(j)
        cnt += 1
print(cnt)
   




    
    
    



