import math
a,b,c = map(int, input().split())

if b > c:
    print(-1)
elif b == c:
    print(-1) 
else:
    print(math.floor(-a / (b - c))+1)

    