

num1=int(input("enter first number"))
num2=int(input("enter  second number"))
num3=int(input("enter third number"))
if(num1>=num2 and num2<=num3):
    print("num1 is largest")
elif(num2>=num3 and num3<=num1):
    print("num2 is largest")
elif(num3>=num1 and num1<=num2):
    print("num3 is largest")