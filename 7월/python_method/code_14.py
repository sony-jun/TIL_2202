x = input()
y = list(x)
con = 0
for i in range(len(y)):
    if y[i] == 'a':
        con += 1
print(con)
