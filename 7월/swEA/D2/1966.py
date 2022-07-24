n = int(input())
for i in range(1,n+1):
    m = int(input())
    numbers = map(int,input().split())
    y = list(numbers)
    y.sort()
    print('#%s' %i,end = ' ')
    print(*y)




        
        
