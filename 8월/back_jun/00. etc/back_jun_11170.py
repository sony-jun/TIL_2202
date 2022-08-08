t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    cnt = 0
    y = list(range(a,b+1))
    for i in y:
        zero = str(i)
        cnt +=zero.count('0')
    print(cnt)
    



    
