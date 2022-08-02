n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    if a + c < b:
        print('advertise')
    elif a +c > b:
        print('do not advertise')
    else:
        print('does not matter')