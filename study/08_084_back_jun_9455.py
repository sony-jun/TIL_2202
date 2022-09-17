t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    in_matrix = list(map(list,zip(*matrix)))

    cnt_0 = []

    for i in in_matrix:
        for j in range(n):
            if i[j] ==1:
                cnt_0.append(i[j:].count(0))
    print(sum(cnt_0))
