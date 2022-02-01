# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

fl_height = float(height)
fl_weight = float(weight)
bmi = round(fl_weight/fl_height**2,1)
if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You are obese")
else:
    print(f"Your BMI is {bmi}. You are clinically obese")