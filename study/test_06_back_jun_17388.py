s, k, h = map(int, input().split())
li = [s, k, h]
if s + k + h >= 100:
    print("OK")
else:
    if min(li) == s:
        print("Soongsil")
    elif min(li) == k:
        print("Korea")
    elif min(li) == h:
        print("Hanyang")
