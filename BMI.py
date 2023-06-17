weight=float(input("enter the weight in kg:"))
height=float(input("enter the height in m :"))
BMI=weight/height*height
if(BMI<18.5):
    print("under weight")
elif(BMI<=18.5 and BMI>=24.9):
    print("normal")
elif(BMI<=25 and BMI>=29.9):
    print("overweight")
elif(BMI>=30):
    print("obese ")
    
    