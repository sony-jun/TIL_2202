n = int(input())
for i in range(n):
    p,q,r,s,w = map(int,input().split())
    a_price = p * w
    if w <=r :
        b_price = q
    else:
        b_price = q +((w-r)*s)
    m = [a_price,b_price]
    print(f'#{i+1} {min(m)}')

