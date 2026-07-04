def show(label,func):
    try:
        func()
    except Exception as e:
        print(f"({type(e).__name__}:{e})")

show("NameError",lambda:print("undefined_variable"))
show("TypeError",lambda:"30"+5)
show("ValueError",lambda:int ("abc"))#right type,bad value
show("IndexError",lambda: [1,2,3][10])
show("KeyError",lambda:{"a":1}["b"])#missing dict key
show("ZeroDivisionError",lambda:1/0)
show("AttributeError",lambda:"hello".push("!"))
show("FileNotFoundError",lambda:open("does_not_exist_12345.txt"))
