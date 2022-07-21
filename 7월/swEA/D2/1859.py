# 아직 고민하고 있는중....
n = int(input())
for i in range(1,n+1):
    day = int(input())
    day_price = list(map(int,input().split()))
    max_day_price = day_price[-1]
    cnt = 0
    for x in range(len(day_price)-1,-1,-1):
        if max_day_price > day_price[x]:
            cnt += max_day_price - day_price[x]
        else:
            max_day_price = day_price[x]
    print("#{} {}".format(i, cnt))

    


