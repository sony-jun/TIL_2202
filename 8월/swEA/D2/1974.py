
t = int(input())
for q in range(1,t+1):
    matrix = []
    for _ in range(9):
        
        numbers = list(map(int,input().split()))
        matrix.append(numbers)
    invese = list(map(list, zip(*matrix)))
    li_1 = []
    for i in matrix:
        
        mum_1 = 1
        for j in range(9):            
            mum_1 *= i[j]
        li_1.append(mum_1)
        

    li_2 = []
    for k in invese:
        
        mum_2 = 1
        for w in range(9):            
            mum_2 *= k[w]
        li_2.append(mum_2)
    li_3 = []    
    for x in range(0,9,3):
        
        for y in range(0,9,3):
            
            mum_3 = 1
            for u in range(3):
                for b in range(3):
                    mum_3 *= matrix[x+u][y+b]
            li_3.append(mum_3)
    cnt = 0
    for choi in range(9):
        if li_1[choi]== li_2[choi] == li_3[choi] == 362880:
            cnt +=1
        else:
            cnt = 0
    if cnt != 9:
        print(f'#{q} 0')
    else:
        print(f'#{q} 1')          

        
    