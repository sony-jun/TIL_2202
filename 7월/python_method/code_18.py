x = input()
dic = {}

for i in x:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
for key in dic.keys():
    print(key,' ', dic[key])