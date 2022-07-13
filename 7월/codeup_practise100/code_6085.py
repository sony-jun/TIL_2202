r, g, b = input().split()

r = float(r)
g = float(g)
b = float(b)

print('%.2f'%float(r*g*b/8/1024/1024),'MB')