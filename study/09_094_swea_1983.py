t = int(input())
per = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for i in range(1, t + 1):
    n, k = map(int, input().split())
    li = []
    for j in range(n):
        mid, fin, res = map(int, input().split())
        total = (mid * 0.35) + (fin * 0.45) + (res * 0.2)
        li.append(total)

    sco = li[k - 1]

    li.sort(reverse=True)
    dig = n // 10
    final = li.index(sco) // dig
    per_ = per[final]

    print(f"#{i} {per_}")

    """
    for num in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    score = []
    for _ in range(n):
        mid, fin, ess = map(int, input().split())
        score.append(mid * 0.35 + fin * 0.45 + ess * 0.2)

    abc = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    sor_score = sorted(score, reverse=True)
    score_abc = {'A+' : [], 'A0' : [], 'A-' : [], 'B+' : [], 'B0' : [], 
                'B-' : [], 'C+' : [], 'C0' : [], 'C-' : [], 'D0' : []}
    n_10 = n // 10

    for i in range(10):
        score_abc[abc[i]] = sor_score[i * n_10 : i * n_10 + n_10] 
        if score[k - 1] in score_abc[abc[i]]:
            print(f'#{num}', abc[i])

    """
