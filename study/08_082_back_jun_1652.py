t = int(input())
matrix = [list(input()) for _ in range(t)] # 입력받은 숫자의 N X N 짜리 행렬(이중리스트)로 만든다
in_matrix = list(map(list,zip(*matrix))) # 전치 행렬을 만들어 준다.

row = [] # 이어진 행 개수를 새고, 그 수를 넣을 빈 리스트 ..X..  
col = [] # 이어진 열 개수를 새고, 그 수를 넣을 빈 리스트

for i in range(t):
    cnt_r = 0
    cnt_c = 0
    for j in range(t):
        if matrix[i][j] == '.':
            cnt_r +=1
        elif matrix[i][j] == 'X':
            row.append(cnt_r) # 행에서, X를 만나지 않았을 때, '.'의 개수를 새어 나간다
            cnt_r = 0         # X를 만나게 되면 카운트를 빈 리스트에 보낸 후 카운트를 0으로 바꿔준다
        if in_matrix[i][j] == '.':
            cnt_c +=1
        elif in_matrix[i][j] == 'X':
            col.append(cnt_c) #열에서, X를 만나지 않았을 때, '.'의 개수를 새어 나간다
            cnt_c =0          # X를 만나게 되면 카운트를 빈 리스트에 보낸 후 카운트를 0으로 바꿔준다
    row.append(cnt_r)         # 행의 마지막에서 카운트를 보내지 않는다면, .....일 경우 아무것도 보내지지 않는다
    cnt_r = 0                 # 보낸 후 다시 카운트를 0으로 초기화 시킨다
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
# 행,렬이 1보다 큰 개수를 카운트 한다
print(row_num,col_num)

