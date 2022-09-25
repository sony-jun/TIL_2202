t = int(input())
for X in range(1,t+1):
    n,k = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)] 
    in_matrix = list(map(list,zip(*matrix))) 

    row = [] 
    col = []

    for i in range(n):
        cnt_r = 0
        cnt_c = 0
        for j in range(n):
            if matrix[i][j] == 1:
                cnt_r +=1
            elif matrix[i][j] == 0:
                row.append(cnt_r) 
                cnt_r = 0         
            if in_matrix[i][j] == 1:
                cnt_c +=1
            elif in_matrix[i][j] == 0:
                col.append(cnt_c) 
                cnt_c =0          
        row.append(cnt_r)         
        cnt_r = 0                 
        col.append(cnt_c)
        cnt_c = 0
    cnt = 0
    for l in row:
        if l == k:
            cnt +=1
    for o in col:
        if o == k:
            cnt +=1
    print(f'#{X} {cnt}')
         