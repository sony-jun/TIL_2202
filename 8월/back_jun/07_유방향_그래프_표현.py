from pprint import pprint 
n,m = map(int,(input().split()))

graph = [[0]*(n+1) for _ in range(n+1)]
gra = [[] for _ in range(n+1)]
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1][v2] = 1
    
    gra[v1].append(v2)
    
pprint(graph)
pprint(gra)
    