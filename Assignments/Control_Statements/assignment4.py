#Program to check whether a Number is divisible by 5 or not.
import sys
number=sys.argv[1]
if int(number)%5==0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")