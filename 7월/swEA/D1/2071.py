n = int(input())
for i in range(n):
    y = map(int,input().split())
    numbers = list(y)
    avg = float((sum(numbers)/len(numbers)))

    print('#%s %s'%(i+1,round(avg)))