# 일단 '(' 와 ')'의 수는 같아야 한다(조건 1)
# ())(() 처럼 조건 1이 충족된다 하더라도 VPS성립 하지 않는 경우가 있음


import sys
input = sys.stdin.readline

number = int(input())
for k in range(number):
    n = list(input())
    sum_ = 0
    for i in n:
        if i == '(':
            sum_ += 1
        elif i == ')':
            sum_ -= 1
    if sum_ < 0:
        print('NO')
    if sum_ > 0:
        print('NO')
    elif sum_ == 0:
        print('YES')
# 이렇게 하면 마지막 ())(() 에서 YES가 나오므로 실패...


# t = int(input())
# for _ in range(t):
#     stk = []
#     s = input()
#     isVPS = True

#     for ch in s:
#         if ch == '(':
#             stk.append('(')
#         if ch == ')':
#             if stk:
#                 stk.pop()
#             elif not stk:
#                 isVPS = False
#                 break
#     if not stk and isVPS:
#         print('YES')
#     elif stk or not isVPS:
#         print('NO')

#접근 방식 자체가 생각 못한 방식이였다 



  
