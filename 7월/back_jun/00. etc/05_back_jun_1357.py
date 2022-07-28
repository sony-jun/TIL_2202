a,b = list(input().split())

x = list(a[::-1])
y = list(b[::-1])

cnt_x = ''
cnt_y = ''
for i in x:
    cnt_x+=i
for j in y:
    cnt_y+=j

mum = (int(cnt_x)+int(cnt_y))
mum_list = list(str(mum))
rev = list(mum_list[::-1])
rev_count = ''
for k in rev:
    rev_count += k
print(int(rev_count))
