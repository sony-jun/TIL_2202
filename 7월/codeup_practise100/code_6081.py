x = int(input(),16)
for i in range(1, 16):
    print('%X'%x, "*", '%X'%i, "=", '%X'%(x*i), sep='')
