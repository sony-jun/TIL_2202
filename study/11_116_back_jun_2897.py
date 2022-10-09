n, m = map(int, input().split())
li = [0, 0, 0, 0, 0]
truck = []
graph = [list(input()) for _ in range(n)]

for i in range(n - 1):
    for j in range(m - 1):
        bin = []
        for k in range(2):
            for w in range(2):
                bin.append(graph[i + k][j + w])
        if "#" not in bin:
            truck.append(bin)

for q in truck:
    if q.count("X") == 0:
        li[0] += 1
    elif q.count("X") == 1:
        li[1] += 1
    elif q.count("X") == 2:
        li[2] += 1
    elif q.count("X") == 3:
        li[3] += 1
    elif q.count("X") == 4:
        li[4] += 1
for liin in li:
    print(liin)
