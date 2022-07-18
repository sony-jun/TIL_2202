a = int(input())

if a == 0:
    print(1)
elif a < 0:
    print('0보타 큰 수를 입력하세요')
    digi = ()
else:
    digi = 0
    while a:
        a //= 10
        digi += 1
    print(digi)
