c = list(map(int, input().split()))
cnt = 0
for i in c:
    cnt+= i**2
print(cnt%10)


