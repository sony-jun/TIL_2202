import sys

input = sys.stdin.readline  # 통과를 위해...

n, m = map(int, input().split())
bang = [0] * (n + 1)  # 0번째를 넣어주기 위해 하나 더 더함
cnt = 0
graph = [[] for i in range(n + 1)]  # 0번째를 넣어주기 위해 역시 하나 더 더함

for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 인접리스트 생성


def dfs(v):  # DFS 함수
    bang[v] = 1  # 0을 1로 바꿈 -> 방문하지 않은 숫자가 들어와서
    for k in graph[v]:
        if not bang[k]:  # 방문하지 않으면
            dfs(k)  # 방문하지 않은 숫자로 dfs 함수 돌려줌


for w in range(1, n + 1):
    if not bang[w]:  # 방문하지 않았을 때
        dfs(w)  # 방문하지 않은 숫자 dfs 함수
        cnt += 1  # 개수 +1
print(cnt)
