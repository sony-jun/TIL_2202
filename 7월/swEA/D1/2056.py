n = int(input())
for i in range(n):
    numbers = input()
    year = numbers[:4]
    mon = numbers[4:6]
    day = numbers[6:8]
    day_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if int(mon) >12 or int(mon) <= 0 :
        print(f'#{i+1} -1')
        continue
    else:
        if day_dict[int(mon)] < int(day) or int(day) <=0:
            print(f'#{i+1} -1')
            continue
        else:
            print(f'#{i+1} {year}/{mon}/{day}')

    
    