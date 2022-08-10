from pprint import pprint

n = int(input())
bu,ja = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)


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
                        
dfs(bu)
# bu를 집어 넣었을 때 ja가 F이면 성립하지 않음
# bu를 집어 넣었을 때 ja가 T이면 성립
# 몇다리를 건너 갔는가를 체크

pprint(visited)






