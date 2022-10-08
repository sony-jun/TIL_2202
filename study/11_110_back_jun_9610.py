t = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
a = 0
for _ in range(t):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1
    else:
        a += 1
print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"Q4: {q4}")
print(f"AXIS: {a}")
