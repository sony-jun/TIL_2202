t = int(input())
for _ in range(t):
    car = int(input())
    bupum = int(input())
    if bupum ==0:
        print(car)
    else:
        mum = car
        for _ in range(bupum):
            a,b = map(int,input().split())
            c = a*b
            mum += c
        print(mum)
    
    
