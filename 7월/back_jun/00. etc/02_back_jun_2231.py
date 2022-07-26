n = int(input())
for i in range(n):
    cnt = 0
    a = sum(list(map(int,str(i))))
    x = i + a
    if x == n:
        cnt = i
        break
print(cnt)
    


