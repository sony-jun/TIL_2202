t = int(input())
for X in range(1, t + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, (input().split()))) for _ in range(n)]
    bin = []

    for x in range(n - m + 1):
        for y in range(n - m + 1):

            cnt = 0
            mul = []

            for i in range(m):
                for j in range(m):

                    mul.append(matrix[x + i][y + j])
            bin.append(sum(mul))
    print(f"#{X} {max(bin)}")


"""
def hap(lst):
    f = 0
    for i in lst:
        f += sum(i)
    return f
for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            ans = max(ans, hap([maps[i + x][j:j + m] for x in range(m)]))
    print(f"#{test_case} {ans}")
"""
