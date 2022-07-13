x = input()
y = list(x)
list.reverse(y)
print(''.join(y))

# ==========================



rep = ''
len = len(x) -1
while len >= 0:
    rep += x[len]
    len -= 1
print(rep)


#==========================
word = 'apple'
result = ''
for i in word:
    result = i + result
print(result)

print(word[::-1])
print(reversed(word))