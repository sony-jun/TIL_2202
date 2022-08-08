li = []
for _ in range(9):
    number = int(input())
    li.append(number)
# 7개의 숫자를 다 더했을 때, 값이 100이 되는 숫자 7개를 구하라.
# 저 말은 곧 총합 - 숫자 2개가 100이 되면 됨
ne_li = []
for i in range(8):
    for j in range(i+1,9):
        mum = sum(li) - (li[i]+li[j])
        if mum ==100:
            ne_li.append(li[i])
            ne_li.append(li[j])
            break


li.remove(ne_li[0])
li.remove(ne_li[1])
y = sorted(li)
for k in y:
    print(k)
    


