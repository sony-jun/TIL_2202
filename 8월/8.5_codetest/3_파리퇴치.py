num = int(input())
for w in range(1,num+1):
    a,b = map(int,input().split())
    matrix = []
    for k in range(a):
        li = list(map(int,input().split()))
        matrix.append(li)
    bin = []
    for x in range(a-b+1):
        for y in range(a-b+1):
            
            mul = []
            for i in range(b):
                for j in range(b):
                    
                    mul.append(matrix[x+i][y+j])
            bin.append(sum(mul))
    print(f'#{w} {max(bin)}')
                    
            
       






    