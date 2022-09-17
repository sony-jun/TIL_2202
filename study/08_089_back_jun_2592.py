li = []
for i in range(10):
    a = int(input())
    li.append(a)
print(round(sum(li)/10))
cnt = []
for j in range(10):
    cnt.append(li.count(li[j]))
cnt_max = max(cnt)
li_max = []
for k in range(10):
    if cnt[k]==cnt_max:
        li_max.append(li[k])
print(min(li_max))

