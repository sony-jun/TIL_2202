while True:
    n = input()
    if n == '#':
        break
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cnt = 0
    for i in range(len(n)):
        if n[i] in vowel:
            cnt +=1
    print(cnt)




