n = int(input())
for i in range(n):
    a,b = input().split()
    for j in b:
        print(j*int(a),end='')
print('')
