n = int(input())

for tc in range(1, n+1):
    num = int(input())
    arr = [[0]*num for _ in range(num)]
 
    for i in range(num):
        for j in range(i+1):
            if j == 0:
                arr[i][j] = 1
            if j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
                
    print('#{}'.format(tc))
    for i in range(num):
        for j in range(num):
            if arr[i][j] != 0:
                print(arr[i][j],end=' ')
        print()