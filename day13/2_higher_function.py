# A function that takes another function as argument is called higher order function
# sorted(),map(),filter(),reduce(),decorators etc are the higher order function in python

# map(function,iterable)
# map takes function as first parameter and iterable as a second parameter
# It maps every element of the iterable to some other form
# The length of initial iterable and final result is same in map

data=[1,2,3,4,5]

def cube(elem):
    return elem**3

result=map(cube,data)
print(result) #<map_object> which is an iterator and can be looped. But to see its element we need to convert 
# it to some other data type
print(list(result))

# for each in list(result):
    # print(each)


# filter(function,iterable)
# It also take function and iterables as arguments
# It picks certain elemets from the initial iterable as per the given condition
# But the size of initial iterables and final result may not be same in case of filter

data=[1,2,3,4,5,6,7,8,9,10]

def get_even(elem):
    return elem%2==0
result=filter(get_even,data)
print(result)
print(list(result))


# reduce(function,iterable)
# It also take function and iterables as arguments
# It does operation based on the  given function and return single value


# reduce is not used likely so we need to import it
from functools import reduce
data=[1,2,3,4,5,6]
def add(x,y):
    return x+y

result=reduce(add,data)
print(result)