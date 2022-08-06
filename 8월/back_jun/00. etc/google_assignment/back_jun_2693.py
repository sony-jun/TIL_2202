n = int(input())
for i in range(n):
    number = list(map(int,input().split()))
    number.sort(reverse=True)
    print(number[2])