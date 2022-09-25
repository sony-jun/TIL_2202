n,m = map(int,(input().split()))
li = list(map(int,(input().split())))
max_ = 0
#  M에 최대한 가까운 카드 3장의 합
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            cnt = li[i]+li[j]+li[k]

            if max_ < cnt <= m:
                max_ = cnt
            if max_ == m:
                break

print(max_)