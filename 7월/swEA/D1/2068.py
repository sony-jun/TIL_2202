n = int(input())
for i in range(n):
    y = map(int,input().split())
    numbers = list(y)
    l = max(numbers)

    print('#%s %s'%(i+1,l))