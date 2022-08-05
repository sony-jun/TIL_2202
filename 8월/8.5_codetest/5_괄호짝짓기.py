for num in range(10):
    stk = []
    number = int(input())
    s = input()
    isVPS = True
    if len(s) != number:
        print(f'#{num+1} 0')
    else:


        for ch in s:
            if ch == '(':
                stk.append('(')
            if ch == ')':
                if stk:
                    stk.pop()
                elif not stk:
                    isVPS = False
                    break
        for ch in s:
            if ch == '<':
                stk.append('<')
            if ch == '>':
                if stk:
                    stk.pop()
                elif not stk:
                    isVPS = False
                    break
        for ch in s:
            if ch == '[':
                stk.append('[')
            if ch == ']':
                if stk:
                    stk.pop()
                elif not stk:
                    isVPS = False
                    break
        for ch in s:
            if ch == '{':
                stk.append('{')
            if ch == '}':
                if stk:
                    stk.pop()
                elif not stk:
                    isVPS = False
                    break
        if not stk and isVPS:
            print(f'#{num+1} 1')
        elif stk or not isVPS:
            print(f'#{num+1} 0')
