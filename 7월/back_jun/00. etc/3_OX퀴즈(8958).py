# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

n = int(input())
for j in range(1,n+1):
    x = input()
    y = list(x)
    cnt = 0
    c = 1
    for i in y:
        if i == 'O':
            cnt += c
            c += 1
        else:
            c = 1                
        
           
    print(cnt)
