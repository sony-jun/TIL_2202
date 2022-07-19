n = int(input())
for i in range(n):
    y = map(int,input().split())
    numbers = list(y)
    m = 0
    for l in numbers:
        
        if l%2 != 0:
            m += l
    print(f'#{i+1} {m}')    
