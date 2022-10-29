a, b = map(int, input().split())

x, y = (a - 1) // 4 + 1, (a - 1) % 4
i, j = (b - 1) // 4 + 1, (b - 1) % 4

print(abs(x - i) + abs(y - j))
