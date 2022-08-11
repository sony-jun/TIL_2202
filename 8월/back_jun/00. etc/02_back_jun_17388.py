# 세 대학의 참여도는 모두 다르다. == 같은 수 고려 X

Soongsil, Korea, Hanyang = map(int,input().split())
if Soongsil + Korea + Hanyang >= 100:
    print('OK')
else:
    y = [Soongsil, Korea, Hanyang]
    y.sort()
    if y[0] == Soongsil:
        print('Soongsil')
    elif y[0] == Korea:
        print('Korea')
    else:
        print('Hanyang')
# 좀 더 간단한 법 없나?
