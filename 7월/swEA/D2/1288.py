n = int(input())
for i in range(n):
    come = int(input())
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    zero = []
    cnt = 1
    for j in range(1,1000000):
        cnt = come*j
        num = str(cnt)
        y = list(num)
        zero.extend(y)
        zeros = sorted(set(zero))
        if zeros == numbers:
            print(f'#{i+1} {cnt}')
            break
        
            





    

