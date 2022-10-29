t = int(input())
for _ in range(t):
    a, b = input().split()
    x = sorted(list(a))
    y = sorted(list(b))

    if x == y:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
