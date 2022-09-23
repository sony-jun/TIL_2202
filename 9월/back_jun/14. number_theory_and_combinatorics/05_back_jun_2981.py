# 제한 1초라 안될꺼 뻔한데 일단 짜봄

t = int(input())
li = []
for _ in range(t):
    a = int(input())
    li.append(a)
min_ = min(li)
cnt = 0


for i in range(len(li)):
    namuge = []
    for j in range(2,min_+1):
        b = li[i]%j
        namuge.append(b)
    print(namuge)


