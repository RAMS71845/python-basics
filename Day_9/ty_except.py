"""
TRY->EXCEPT->ELSE->FINALLY
"""


def to_int(text):
    try:
        return int(text)
    except ValueError:
        return None
    
print(to_int(34))
print(to_int("ABC"))

def safe_divide(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        print(f"{a}/{b}: cannot divide by zero")
    else:
        print(f"{a}/{b}={result}")
    finally:
        print("ITS DONE")

safe_divide(5,0) 