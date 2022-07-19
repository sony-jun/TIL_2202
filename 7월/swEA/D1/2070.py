n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a == b:
        print('#%s ='%(i+1))
    elif a > b:
        print('#%s >'%(i+1))
    else:
        print('#%s <'%(i+1))
