# 첩보원명은 알파벳 대문자, 숫자 0~9, 
# 대시 (-)로만 이루어져 있으며, 최대 10글자
# 둘다 별로 중요한 정보 아니었음
y = []
for i in range(1,6):
   
    n = input()
    if n.count('FBI') >=1:
        y.append(i)
if y ==[]:
    print('HE GOT AWAY!')
else:
    print(*y)

