a, b = map(int, input().split())

li = []
cnt_1 = 1
cnt_2 = 1
for i in range(a, 0, -1):
    li.append(i)
for k in range(b):
    cnt_1 *= li[k]

for j in range(1, b + 1):
    cnt_2 *= j

print(round(cnt_1 / cnt_2))
