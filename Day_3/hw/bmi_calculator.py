weight=float(input("Enter your weight :"))
height=float(input("Enter your height :"))
bmi=weight/(height**2)
if bmi<18.5:
    Category="Underweight"
elif bmi<25:
    Category="Normal"
elif bmi<30:
    Category="Overweight"
else:
    Category="Obese"
print(f"Your BMI is {bmi:.1f}->{Category}")