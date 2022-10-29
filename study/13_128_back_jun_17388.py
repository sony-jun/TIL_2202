Soongsil, Korea, Hanyang = map(int, input().split())
if Soongsil + Korea + Hanyang >= 100:
    print("OK")
else:
    y = [Soongsil, Korea, Hanyang]
    y.sort()
    if y[0] == Soongsil:
        print("Soongsil")
    elif y[0] == Korea:
        print("Korea")
    else:
        print("Hanyang")
