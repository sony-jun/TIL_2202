x, y = input().split()
n = int(x)
m = int(y)
def area(n,m):
    return n * m
def round(n,m):
    return 2*(n+m)
def rectangle(n,m):
    return (area(n,m), round(n,m))
print(rectangle(n,m))
