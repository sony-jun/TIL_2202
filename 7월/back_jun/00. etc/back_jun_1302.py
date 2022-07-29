n = int(input())
b_name = []
dic = {}
for i in range(n):
    m = input()
    if m in dic:
        dic[m] += 1
    else:
        dic[m] = 1

y = max((dic.values()))

b_cnt = []

for j in dic:
    if dic[j] == int(y):
        b_cnt.append(j)
b_cnt.sort()
print(b_cnt[0])
