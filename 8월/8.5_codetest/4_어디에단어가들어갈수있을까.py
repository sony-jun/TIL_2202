num = int(input())
for z in range(1,num+1):
    g,h = map(int,input().split())
    matrix = [list(input().split()) for _ in range(g)]
    in_matrix = [[0]*g for _ in range(g)]

    for j in range(len(matrix[0])):
        for i in range(g):
            in_matrix[j][i] = matrix[i][j]
    row = []
    row_0 = 0
    column = []
    column_0 = 0
    for k in matrix:
        for w in range(len(k)):
            if k[w] == '1':
                row_0 +=1          
            elif k[w] == '0':
                row.append(row_0)
                row_0=0
        row.append(row_0)
        row_0 = 0    
        
    row.append(row_0)


    for a in in_matrix:
        for b in range(len(a)):
            if a[b] =='1':
                column_0 +=1
            elif a[b] == '0':
                column.append(column_0)
                column_0=0
        column.append(column_0)
        column_0 = 0
    column.append(column_0)
            
    row_num = 0            
    col_num = 0
    for _ in row:
        if _ == h:
            row_num +=1
    for _ in column:
        if _ ==h:
            col_num +=1
    
    print(f'#{z} {row_num+col_num}')
