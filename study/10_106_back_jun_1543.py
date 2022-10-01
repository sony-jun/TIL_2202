"""
n = input()
c = input()
print(n.count(c)) 
"""
# 통과 못하는 코드
n = input()
c = input()
cnt = 0
b = n

while True:
    if c not in n:
        break
    if c in n:
        cnt += 1
        b = n.replace(c, "", cnt)
        if c not in b:
            break
print(cnt)
