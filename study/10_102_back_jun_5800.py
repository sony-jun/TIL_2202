t = int(input())
for _ in range(1,t+1):
    li = list(map(int,input().split()))
    li_so = sorted(li[1:])
    gaps = []
    for i in range(len(li_so)-1):
        gap = li_so[i+1] - li_so[i]
        gaps.append(gap)
    print(f'Class {_}')
    print(f'Max {max(li[1:])}, Min {min(li[1:])}, Largest gap {max(gaps)}')