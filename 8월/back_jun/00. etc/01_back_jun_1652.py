num = int(input())
matrix = [list(input()) for _ in range(num)]
in_matrix = [[0]*num for _ in range(len(matrix[0]))]

for j in range(len(matrix[0])):
    for i in range(num):
        in_matrix[j][i] = matrix[i][j]
row = []
row_0 = 0
column = []
column_0 = 0
for k in matrix:
    for w in range(len(k)):
        if k[w] == '.':
            row_0 +=1          
        elif k[w] == 'X':
            row.append(row_0)
            row_0=0
    row.append(row_0)
    row_0 = 0    
        
row.append(row_0)


for a in in_matrix:
    for b in range(len(a)):
        if a[b] =='.':
            column_0 +=1
        elif a[b] == 'X':
            column.append(column_0)
            column_0=0
    column.append(column_0)
    column_0 = 0
column.append(column_0)
            
row_num = 0            
col_num = 0
for _ in row:
   if _ > 1:
    row_num +=1
for _ in column:
    if _ >1:
        col_num +=1

print(row_num,col_num)



    
