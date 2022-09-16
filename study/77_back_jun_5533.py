t = int(input())
matrix = []
for i in range(t):
    a = list(map(int,input().split()))
    matrix.append(a)


in_matrix = [[0 for _ in range(t)] for _ in range(3)]

for j in range(t):
    for k in range(3):
        in_matrix[k][j] = matrix[j][k]

for w in range(3):
    for o in range(len(matrix)):
        if in_matrix[w][0] == in_matrix[w][o]:
            in_matrix[w][o]=0
print(in_matrix)




