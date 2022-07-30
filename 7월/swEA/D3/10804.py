

n = int(input())
for i in range(n):
    nop = list(input())
    y = nop[::-1]
    mirror = []
    char = ''
    for j in y:
        if j == 'b':
            mirror.append('d')
        elif j == 'd':
            mirror.append('b')
        elif j == 'p':
            mirror.append('q')
        elif j == 'q':
            mirror.append('p')
    for k in mirror:
        char += k

    print(f'#{i+1} {char}')


