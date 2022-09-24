t = int(input())
for X in range(1,t+1):
    n,m = map(int,input().split())
    matrix = [list(map(int,(input().split()))) for _ in range(n)]
    bin = []

    for x in range(n - m + 1):
        for y in range(n - m + 1):
            
            cnt = 0
            mul = []

            for i in range(m):
                for j in range(m):

                    mul.append(matrix[x+i][y+j])
            bin.append(sum(mul))
    print(f'#{X} {max(bin)}')
    
            
    