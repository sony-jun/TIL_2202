a, b, c = map(int, input().split())
number = []
dic = {}

for _ in range(3):
    #  트럭의 수에 따라서 주차 요금을 할인해 준다.
    x, y = map(int, input().split())
    li = list(range(x, y))
    number.append(li)
    # 첫번째 = 1~6 12345
    # 두번째 = 3~5   34
    # 세번째 = 2~8  234567
    # 34일때 1원 *3대 * 2분 = 6
    # 2,5일때 3원 * 2대 * 2분 = 12
    # 1,6,7 일때 5원 *1대 * 3분 = 15   33!
    # 같은게 3개일때 cnt3, 2개일때 cnt2 1개일 때 cnt1
    # for 로는 중복 확인 불가
    # 딕셔너리?
for i in number[0]:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for j in number[1]:
    if j in dic:
        dic[j] += 1
    else:
        dic[j] = 1
for k in number[2]:
    if k in dic:
        dic[k] += 1
    else:
        dic[k] = 1

counts = list(dic.values())
cnt3 = counts.count(3)
cnt2 = counts.count(2)
cnt1 = counts.count(1)

print(cnt1 * a + cnt2 * b * 2 + cnt3 * c * 3)
