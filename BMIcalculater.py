print("Welcome to BMI Calculater!!")
weight=float(input("Enter your Weight : "))
height=float(input("Enter your Height : "))
bmi=weight/(height*height)
final_bmi=round(bmi,2)
print(final_bmi)
if bmi <18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are normal weight")
elif bmi < 30:
    print("you are over weight")
elif bmi < 35:
    print("you are obese")
else:
    print("you are clinically obese")