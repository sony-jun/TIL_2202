t = int(input())
li = []
for i in range(2900000):
    li.append(str(i))
nu_li = []
for j in li:
    if '666' in j:
        nu_li.append(j)
print(nu_li[t-1])

# 런타임 에러 발생...시간을 어떻게 줄여야 할까?
# range값이 너무 적어서 런타임에러(index error)발생함
# 충분한 값으로 넣어주니 클리어
    
# str(i) + '666'

#'666' + str(j)

# 66601 이런 01 012이런 값이 들어가지 않음


