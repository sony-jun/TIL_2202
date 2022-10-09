t = int(input())
li = [0, 0, 0, 0, 0]
for _ in range(t):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        li[0] += 1
    elif x < 0 and y > 0:
        li[1] += 1
    elif x < 0 and y < 0:
        li[2] += 1
    elif x > 0 and y < 0:
        li[3] += 1
    else:
        li[4] += 1
print(f"Q1: {li[0]}")
print(f"Q2: {li[1]}")
print(f"Q3: {li[2]}")
print(f"Q4: {li[3]}")
print(f"AXIS: {li[4]}")
