i=1
j=1
number=1
while i <= 6:
    j=1
    while j <= 6:
        if i==1 or j==1 or j==6:
            print("*",end=' ')
            number+=1
            j+=1
        else:
            print(" ",end=' ')
            j+=1
    print()
    i+=1
k=1
l=1
while k <= 6:
    l=1
    while l <= 6:
        if k==1 or l==1 or l==6:
            print("-",end=' ') or k==3 
            number+=1
            l+=1
        else:
            print(" ",end=' ')
            l+=1
    print()
    k+=1
