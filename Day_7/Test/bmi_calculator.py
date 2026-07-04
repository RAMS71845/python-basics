def bmi():
    weight_kg=float(input("Enter Your weight"))
    height_m=float( input("Enter your height"))
    bmi=weight_kg/(height_m**2)
    return bmi,weight_kg,height_m
calculated_bmi,weight,height=bmi()
print(f"Expected : {calculated_bmi:.1f}")
