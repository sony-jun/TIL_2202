list_ = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G','E']

word = input()
for char in list_ :
    word = word.replace(char, "")
print(word)