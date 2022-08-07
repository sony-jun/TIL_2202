t = int(input())
for i in range(1,t+1):
    n = int(input())
    li = ''
    
    for j in range(n):
        char,cnt = input().split()
        li+=(char*int(cnt))
    print(f'#{i}')
    for k in range(0,len(li),10):
        print(li[k:k+10])





