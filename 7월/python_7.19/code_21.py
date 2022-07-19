n = int(input())
cnt = 0
while n!=0:
    cnt *=10
    cnt += n % 10
    n //= 10
print((cnt))
    
    


