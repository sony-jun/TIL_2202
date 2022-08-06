li = []
dic = {}
for i in range(10):
    n = int(input())
    li.append(n)
print(round(sum(li)/10))
for j in li:
    if j  in dic:
        dic[j] += 1
    else:
        dic[j] =1
k = max(dic.values())
for key,value in dic.items():
    if value ==k:
        print(key)
