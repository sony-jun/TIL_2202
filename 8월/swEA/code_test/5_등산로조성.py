import sys

sys.stdin = open("_등산로조성.txt")
t = int(input())
dydx = [[-1,0],[0,1],[1,0],[0,-1]]
dy = [-1, 0, 1,  0] 
dx = [ 0, 1, 0, -1]
for p in range(1,t+1):
    n,k = map(int,input().split())
    
    maps = []
    
    for q in range(n):
        gil = list(map(int,input().split()))
        maps.append(gil)
    max_high = 0
    for i in range(n):
            max_ = max(maps[i])
            if max_high < max_:
                max_high = max_
    # 가장 높은 점의 좌표를 알기위해 리스트로 좌표를 넣어준다   
    bin_ = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == max_high  :
                bin_.append([i,j])
              
    # 빼는 k값을 구하는거 말고 그냥 경로를 구하는거부터 해보자
    for w in range(n):
        for o in range(n):
            for gi in range(len(dydx)):
   
                for high in range(len(bin_)):
                    ny = dydx[gi][0] + bin_[high][0]
                    nx = dydx[gi][1] + bin_[high][1]
                    if 0 < nx <= n and 0 < ny <= n:
                        break
                    if maps[ny][nx] < maps[ny+1][nx+1]:
                        break
    #한 번 이동할 때 마다 하나를 체크해야 하는데...어떻게 하지?                    


    print(f'#{p} {(bin_)}')
    

