#program to find whether a given year is a leap year or not
year=input("Enter the year: ")
if int(year)%4==0:
    print("The entered year is leap year")
else:
    print("The entered year is not a leap year")