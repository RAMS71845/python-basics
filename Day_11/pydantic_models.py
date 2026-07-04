#pip install pydantic
from pydantic import BaseModel,Field,ValidationError

class Product(BaseModel):
    name:str
    price: float = Field(gt=0)#greater than 0
    tags:list [str]=[]

pen= Product(name="GelPen",price=10,tags=["pens"])
print(pen)
# item=Product(name= "Broken",price=-5)
# print(item)#an error will come becoz we declare price as float but assigned with a-5
try: 
    Product(name='Broken',price=-5)
except ValidationError as err:
    print("Caught Validation error")
    print(err.errors()[0]["msg"]) 