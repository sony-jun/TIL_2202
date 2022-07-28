cnt = []
for i in range(10):
    n = int(input())
    j = n%42
    cnt.append(j)
m = list(set(cnt))
print(len(m))


