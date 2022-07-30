

n = int(input())
for i in range(n):
    nop = int(input())
    money = list(map(int,input().split()))
    average = sum(money) / nop
    or_not = []
    for j in money:
        if average >= j:
            or_not.append(j)
    print(f'#{i+1} {len(or_not)}')



