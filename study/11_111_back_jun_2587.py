li = []
for _ in range(5):
    li.append(int(input()))

y = sorted(li)
print(round(sum(li) / 5))
print(y[2])
