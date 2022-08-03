# 행은 비교  x, 열이 같을때만 비교!


n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
num = []
# 각 열 즉, ex) [x][0]가 같은 값이면, 모두 0으로 바꿔라


for i in range(n):
    for j in range(3):
        if matrix[i][j] == matrix[not i][j]:
            matrix[i][j] = 0
            matrix[not i][j] = 0
print(matrix)

             
            


            



    
        


