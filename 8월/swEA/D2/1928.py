t = int(input())
for _ in range(1,t+1):
    char = list(input())
    base64 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/'
          ]
 
    byun = ''
    for i in range(len(char)):
        num = base64.index(char[i])
        bin_num = str(bin(num)[2:])
        while len(bin_num) <6:
            bin_num = '0' + bin_num
        byun += bin_num
    r = ''
    for w in range((len(char)*6)//8):
 
       
        e = int(byun[w*8:w*8+8],2)
 
        
        r += chr(e)
    print(f'#{_} {r}')




