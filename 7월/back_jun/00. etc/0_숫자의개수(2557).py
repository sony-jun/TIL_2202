# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)
y = list(mul)
for i in range(10):
    print(y.count(str(i)))
