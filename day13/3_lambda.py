# Lambda are the elegant way of creating one-liner function
# Lambda functions donot have name. so, they are also called anonymous functions

def squared(num):
    return num**2
print(squared(2)) #4

squared=lambda num:num**2
print(squared(4))
# this is not recomended use of lambda

# the proper use of lambda function
# lambda can be called inside the map(),filter(),reduce() as an function argumet
# map()
data=[1,2,3,4,5]
result=map(lambda num:num**3,data)
print(result)
print(list(result))
result=filter(lambda elem:elem%2==0,data)
print(result)
print(list(result))#(1,2,3,4,5)


# filter()
data=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda elem:elem%2==0,data)
print(result)
print(list(result))
result=map(lambda num:num**3,data)
print(result)
print(list(result))#(False,True.....,False,True)

# reduce()
from functools import reduce
data=[1,2,3,4,5,6]
result=reduce(lambda x,y:x+y,data)
print(result)