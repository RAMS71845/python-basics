from typing import Optional
name:str ="Ram"
# Roll_no:int=45
# print(name)
# name=234
# print (name)
age:int=31
price:float=79.99
is_member:bool=True
tag:list[str]=["AI","PYTHON"]
scores:dict[str,int]={"Math":95,"Science":96}
nickname:Optional[str]=None#either the value is str or none that means it gives options

def total_price(price:float,quantity:int)->float:
    return price*quantity