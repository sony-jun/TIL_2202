n = input().upper()
y = list(n)
cnt = 0
for i in y:
    if i =='A' or i =='B' or i =='C':
        cnt = cnt + 3
    elif i =='D' or i =='E' or i =='F':
        cnt = cnt + 4
    elif i =='G' or i =='H' or i =='I':
        cnt = cnt + 5
    elif i =='J' or i =='K' or i =='L':
        cnt = cnt + 6
    elif i =='M' or i =='N' or i =='O':
        cnt = cnt + 7
    elif i =='P' or i =='Q' or i =='R' or i =='S':
        cnt = cnt + 8
    elif i =='T' or i =='U' or i =='V':
        cnt = cnt + 9
    elif i =='W' or i =='X' or i =='Y' or i =='Z':
        cnt = cnt + 10
print(cnt)

    

