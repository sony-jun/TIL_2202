import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

cnt = int(input()) #3 번 굴림
for k in range(cnt): 
    mum = 0 # list []
    i,j, x, y = map(int,input().split())
    # matrix[i-1][j-1]부터 matrix[x-1],[y-1]까지 있는 모든 값을 더하라
    for w in range(i-1,x):
        for v in range(j-1,y):
            mum += matrix[w][v] #list.append() 이렇게하면 시간이 오래걸림
    print(mum)

    #부분합 nj[x2][y2]에서, nj[x2][y1-1] + nj[x1-1][y2] - nj[x1-1][y1-1] 