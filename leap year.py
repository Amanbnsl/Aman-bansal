year=int(input("enter the year"))
if(year%400==0 and year%100):
    print("the year is leap year")
elif(year%4==0 and year!=100):
    print("year is leap")
else:
    print("not a leap year")