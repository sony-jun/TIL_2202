matrix = []
for _ in range(4):
    i,j,x,y = map(int, input().split())

    for a in range(i,x):
        for b in range(j,y):
            matrix.append([a,b])

se_ma = []

for c in matrix:
    if c not in se_ma:
        se_ma.append(c)
print(len(se_ma))

