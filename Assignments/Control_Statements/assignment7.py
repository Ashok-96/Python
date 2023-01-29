#program to find the largest of two numbers
import sys
f,n1, n2=sys.argv
if int(n1)>int(n2):
    print(f'{n1} is greater')
else:
    print(f'{n2} is greater')
