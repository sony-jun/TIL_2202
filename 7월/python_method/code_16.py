x = input()
y = list(x)
con = 0
for i in range(len(y)):
    if y[i] == 'a' or y[i] == 'e' or y[i] == 'i' or y[i] == 'o' or y[i] == 'u' :
        con += 1
print(con)
