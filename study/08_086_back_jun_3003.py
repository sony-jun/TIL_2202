chess = [1, 1, 2, 2, 2, 8]

pieces = list(map(int, input().split()))

li = []

for i in range(6):
    li.append(chess[i]-pieces[i])
print(*li)
