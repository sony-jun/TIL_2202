n = int(input())
for i in range(n):
    a,b = input().split()
    a = int(a)
    print(b[:a-1]+b[a:])
    
