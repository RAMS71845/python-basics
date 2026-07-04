"""
*args(Extra positionals->tuple)        argsk alava kuch bhi askta hai 
**Kwargs(Extra keywords)->             kwargs alava kuch bhi likhlo 
"""

def total(*args):
    print("args is a tuple",args)
    return sum(args)

print(f"total (10,20,30,40)= {total(10,20,30,40)}")
print(f"total (10,40)= {total(10,40)}")
print(f"total ()= {total()}")

def make_user(**data):
    print("DATA is a dict: ",data)
    return data
make_user(name="Ram",age=34,city="Lucknow")
make_user(name="BENTENISON")
