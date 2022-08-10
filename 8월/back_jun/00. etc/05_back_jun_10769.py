char = input() # 인풋을 str로 받습니다

sad = char.count(':-(')
happy = char.count(':-)')

if sad == happy ==0: # 아무것도 없다면
    print('none')
else:
    if sad > happy : 
        print('sad')
    elif sad < happy :
        print('happy')
    else:
        print('unsure')

    
