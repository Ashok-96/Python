#program to find the largest of three numbers.
#program to find the largest of two numbers
import sys
f,n1, n2, n3=sys.argv
if int(n1)>int(n2) and int(n1)>int(n3):
    print(f'{n1} is greater')
elif int(n2)>int(n3):
    print(f'{n2} is greater')
else:
    print(f'{n3} is greater')
