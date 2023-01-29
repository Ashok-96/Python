#program to check whether a given number is even or odd
import sys
number=sys.argv[1]
if int(number)%2==0:
    print("The number is even")
else:
    print("The number is odd")