"""
Lambda functions-Throwaway function you write inline (no def, no name)
"""

def square_def(n):
    return(n*n)
#LAMBDA

square_lambda=lambda n:n*n
print(square_def(10))#def
print(square_lambda(10))#lambda

sub=lambda a,b:a-b
add=lambda a,b:a+b
print(add(2,4))
print(sub(2,3))

nums=[1,2,3,4,5,6]
#map: apply a function to every item.
double=list(map(lambda n:n*2,nums))
print(double)

test=map(lambda n:n*2,nums)
print(map)#<class 'map'>

#filter

evens=list(filter(lambda n:n%2==0,nums))
print(evens)