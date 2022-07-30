# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

n,m = map(int,input().split())

a = (n %10 * 100) + (n //10%10*10) + (n // 100)  
b = (m %10 * 100) + (m //10%10*10) + (m // 100) 

print(max(a,b))
    


