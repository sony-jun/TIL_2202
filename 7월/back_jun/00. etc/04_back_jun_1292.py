# 1을 1번 2를 2번......n을 n번 넣기
a,b = map(int,input().split())
cnt = ''

for i in range(1,100):
    n = f'{i} ' * i
    cnt +=n
y= list(map(int,cnt.split( )))

print(sum(y[a-1:b]))