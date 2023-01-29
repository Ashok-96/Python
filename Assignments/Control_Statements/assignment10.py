#Program to input Marks of five Subjects Physics ,Chemistry,    Biology, Mathematics and Computer.Calculate Percentage and Grade according to 
#program to check  whether a triangle can be formed by the given value for the angles.
import sys
f,Physics, Chemistry, Biology, Mathematics, Computer =sys.argv
total=int(Physics)+int(Chemistry)+int(Biology)+int(Mathematics)+int(Computer)
percentage=int(total)/int(5)
print(percentage)

if percentage >=90:
    print("Grade S")
elif percentage >=80:
    print("Grade A")
elif percentage >=70:
    print("Grade B")
elif percentage >=60:
    print("Grade C")
elif percentage >=50:
    print("Grade D")
elif percentage >=40:
    print("Grade E")
elif percentage <40:
    print("Fail")   

