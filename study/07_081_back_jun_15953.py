t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    a_money = 0
    b_money = 0
    if a == 1:
        a_money = 5000000
    elif 1 < a <= 3:
        a_money = 3000000
    elif 3 < a <= 6:
        a_money = 2000000
    elif 6 < a <= 10:
        a_money = 500000
    elif 10 < a <= 15:
        a_money = 300000
    elif 15 < a <= 21:
        a_money = 100000
    else:
        a_money = 0
    if b == 1:
        b_money = 5120000
    elif 1 < b <= 3:
        b_money = 2560000
    elif 3 < b <= 7:
        b_money = 1280000
    elif 7 < b <= 15:
        b_money = 640000
    elif 15 < b <= 31:
        b_money = 320000
    else:
        b_money = 0
    print(a_money + b_money) 
