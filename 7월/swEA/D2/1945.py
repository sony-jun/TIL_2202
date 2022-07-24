m = int(input())
for i in range(1,m+1):
    n = int(input())
    cnt_2 = 0
    cnt_3 = 0
    cnt_5 = 0
    cnt_7 = 0
    cnt_11 = 0
    while n != 1 :
        if n % 2 == 0 :
            cnt_2 += 1
            n = n /2
        elif n % 3 == 0 :
            cnt_3 += 1
            n = n / 3
        elif n % 5 == 0 :
            cnt_5  += 1
            n = n / 5
        elif n % 7 == 0 :
            cnt_7 += 1
            n = n / 7
        elif n % 11 == 0 :
            cnt_11 += 1
            n = n/ 11

    print(f'#{i} {cnt_2} {cnt_3} {cnt_5} {cnt_7} {cnt_11}')