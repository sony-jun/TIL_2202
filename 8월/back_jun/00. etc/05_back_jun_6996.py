t = int(input())
for _ in range(t):
    a,b = input().split()
    #하나 역순으로 하고 같냐 다르냐 비교 가 아니라
    # 알파벳이 같으냐 비교
    #문제를 잘못 이해함 ㅋ
    x = sorted(list(a))
    y = sorted(list(b))

    if x == y:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
    
