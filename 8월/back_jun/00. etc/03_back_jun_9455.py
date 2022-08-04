num = int(input())
for _ in range(num):
    x,y = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(x)]
    in_matrix = [[0]*x for _ in range(len(matrix[0]))]

    cnt = 0

    for j in range(len(matrix[0])):
        for i in range(x):
            in_matrix[j][i] = matrix[i][j]
    n_m =[]
    for k in in_matrix:
        for q in range(len(k)):
            if k[q] == 1:
                n_m.append(k[q:].count(0))
    print(sum(n_m))

 


   

    