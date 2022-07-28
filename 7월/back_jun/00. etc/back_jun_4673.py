m = []
n = []
for j in range(1,10001):
    n.append(j)

for i in range(1,10001):
    a = i + sum(list(map(int,str(i))))
    m.append(a)
result = sorted(list(set(n)-set(m)))
for k in result:
    print(k)



    