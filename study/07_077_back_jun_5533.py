t = int(input())
matrix = []
for i in range(t):
    a = list(map(int,input().split()))
    matrix.append(a)


in_matrix = [[0 for _ in range(t)] for _ in range(3)]

for j in range(t):
    for k in range(3):
        in_matrix[k][j] = matrix[j][k]
cnt=[[],[],[]]
for w in range(3):
   
    for o in range(len(matrix)):
        if in_matrix[w].count(in_matrix[w][o]) ==1:
            cnt[w].append(in_matrix[w][o])
        else:
            cnt[w].append(0)
for u in range(t):
    mum = 0
    for b in range(3):
        mum += cnt[b][u]
    print(mum)