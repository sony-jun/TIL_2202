# 행렬로도 풀 수 있을꺼 같지만 너무복잡해짐
# 수의 규칙을 이용해서 풀자
a,b = map(int,input().split())

x,y = (a-1)//4+1,(a-1)%4
i,j = (b-1)//4+1,(b-1)%4

print(abs(x-i)+abs(y-j))

