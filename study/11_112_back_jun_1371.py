import sys

input = sys.stdin.read

n = input()
li = []
dic = {}
for i in n:
    if i != " " and i != "\n":
        li.append(i)
for j in li:
    if j in dic:
        dic[j] += 1
    else:
        dic[j] = 1
max_ = max(dic.values())
choi_bin = []
for key, value in dic.items():
    if value == max_:
        choi_bin.append(key)
choi_bin.sort()
for k in choi_bin:
    print(k, end="")
