#program to check  whether a triangle can be formed by the given value for the angles.
import sys
f,a1, a2, a3=sys.argv
sum=int(a1)+int(a2)+int(a3)
if sum==180:
    print("Triangle can be formed!")
else:
    print("Triangle can't be formed!")
