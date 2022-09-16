n, m = map(int, input().split())
matrix = []

x = 0
y = 0
for i in range(n):
    a = list(input())
    matrix.append(a)

# in_matrix = list(map(list, zip(*matrix)))

in_matrix = [[0 for n in range(n)] for m in range(m)]

for p in range(n):
    for q in range(m):
        in_matrix[q][p] = matrix[p][q]

for j in matrix:
    if 'X' not in j:
        x +=1
for k in in_matrix:
    if 'X' not in k:
        y +=1
print(max(x,y))







