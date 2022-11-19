i=1
j=1
for i in range(1,5):
    for j in range(1,5):
        if (i+j)==5-1:
            print('/',end='')
        elif (i+j)>=(4*i):
            print("\\",end='')
        else:
            print(" ",end='')
    print('')
