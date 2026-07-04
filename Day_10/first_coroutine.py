import asyncio

async def greet(name):
    print(f".......waiting to greet{name}")
    await asyncio.sleep(1) #nonblocking
    return f"Hello {name}"

# maybe=greet("Ram")
# print("Greet (Ram) gave us:" ,maybe)        #using these four will not give output
# print("Type: ",type(maybe).__name__)
# maybe.close()

result1 = asyncio.run(greet("sikha"))
result2=asyncio.run(greet("Ram"))
print("Result",result1)
print("Result ",result2)