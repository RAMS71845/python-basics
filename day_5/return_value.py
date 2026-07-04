# def add(a,b):
#     return a+b
# total=add(4,5)
# print(total)
# print(add(9,8))

# def safe_divide(a,b):
#     if b==0:
#         return "Cannot divide by 0"
#     return a/b
# result=safe_divide(4,2)
# print(result)

#function can also return multiple values 
#python puts them ia a tuple (important)

def min_max_avg(numbers):
    return min(numbers),max(numbers),sum(numbers)/len(numbers)

scored=[65,58,47,58,25]
print (min_max_avg(scored))#this will make it give output in tuple form
#if i want the outputs in seperately
low,high,avg=min_max_avg(scored)
print(f"Lowest : {low},Highest: {high},Avg: {avg:.2f}")