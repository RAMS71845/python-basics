def c_to_f(c):
    return c*9/5+32
def f_to_c(f):
    return (f-32)*5/9
celsius=float(input("Enter temperature in celsius"))

fahrenheit=c_to_f(celsius)
print(f"{celsius:.1f}C ={fahrenheit:.1f}F")
back=f_to_c(fahrenheit)
print(f"Convertin fahrenheit value back to celsius= {back:.1f}C" )
if celsius ==back:
    print("YES, celsius and fahrenheit conversions are correct as we get ORIGINAL celsius value back")
else:
    print("wrong value of CELSIUS") 