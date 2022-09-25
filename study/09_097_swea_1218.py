for _ in range(1,11):
    number = int(input())
    gualho = list(input())
    li_1 = []
    li_2 = []
    li_3 = []
    li_4 = []
    cnt = True

    for i in range(number):
        if gualho[i] == '(':
            li_1.append(gualho[i])
        if gualho[i] == ')':
            if len(li_1) >=1:
                li_1.pop()
            else:
                cnt = False
                break
    for i in range(number):
        if gualho[i] == '{':
            li_2.append(gualho[i])
        if gualho[i] == '}':
            if len(li_2) >=1:
                li_2.pop()
            else:
                cnt = False
                break
    for i in range(number):
        if gualho[i] == '[':
            li_3.append(gualho[i])
        if gualho[i] == ']':
            if len(li_3) >=1:
                li_3.pop()
            else:
                cnt = False
                break
    for i in range(number):
        if gualho[i] == '<':
            li_4.append(gualho[i])
        if gualho[i] == '>':
            if len(li_4) >=1:
                li_4.pop()
            else:
                cnt = False
                break
    if (len(li_1)+len(li_2)+len(li_3)+len(li_4)) > 0 :
        cnt = False
    if cnt == True:
        t = 1
    else:
        t = 0
    print(f'#{_} {t}')


    
