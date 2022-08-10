T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N == M :
        max = 0
        for i in range(N) :
            max += A[i] * B[i]
    else :
        if N > M :
            sum = [0] * (N-M+1)
            for i in range(len(sum)) :
                for j in range(-1, -M-1, -1) :
                    sum[i] += A[j-i] * B[j]
        else :
            sum = [0] * (M-N+1)
            for i in range(len(sum)) :
                for j in range(-1, -N-1, -1) :
                    sum[i] += A[j] * B[j-i]
        
        sum.sort()
        max = sum[-1]
    print(f'#{t} {max}')









