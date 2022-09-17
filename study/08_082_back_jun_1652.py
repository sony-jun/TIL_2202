t = int(input())
matrix = [list(input()) for _ in range(t)]
in_matrix = list(map(list,zip(*matrix)))

row = []
col = []

for i in range(t):
    cnt_r = 0
    cnt_c = 0
    for j in range(t):
        if matrix[i][j] == '.':
            cnt_r +=1
        elif matrix[i][j] == 'X':
            row.append(cnt_r)
            cnt_r = 0
        if in_matrix[i][j] == '.':
            cnt_c +=1
        elif in_matrix[i][j] == 'X':
            col.append(cnt_c)
            cnt_c =0
    row.append(cnt_r)
    cnt_r = 0
    col.append(cnt_c)
    cnt_c = 0  

row_num = 0            
col_num = 0
for _ in row:
   if _ > 1:
    row_num +=1
for _ in col:
    if _ >1:
        col_num +=1

print(row_num,col_num)

