from pprint import pprint
num = int(input())
for _ in range(num):
    matrix = [list(input()) for _ in range(num)]
    bin = [[0]*(len(matrix[0])) for _ in range(num)]
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix)-1):
            if matrix[i][j] == '*':
                bin[i][j] =='*'

                bin[i][j-1] +=1
                bin[i][j+1] +=1
                bin[i-1][j-1] +=1
                bin[i-1][j] +=1
                bin[i-1][j+1] +=1
                bin[i+1][j-1] +=1
                bin[i+1][j] +=1
                bin[i+1][j+1] +=1
                
                
    pprint(bin)



