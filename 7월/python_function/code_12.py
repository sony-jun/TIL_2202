x = input()
y = list(x)

for i in range(len(y)):
    if y[i] == 'a':
        y[i] = ''
print(''.join(y))
        

#=============================================
word = 'apple'
result = ''
for i in 'apple':
    if i !='a':
        result = result + i
print(result)