def c_to_f(temp):
    return temp*9/5+32
def f_to_c(f):
    return (f-32)*5/9
celsius=float(input("Enter temperature in celsius"))

fahrenheit=c_to_f(celsius)
print(f"# expected: ={fahrenheit:.1f}F")
back=f_to_c(fahrenheit)
print(f"# expected: {back} (default to'c')")
