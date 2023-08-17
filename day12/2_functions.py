# functions are the blocks of reusuable codes.
# They are defined at a place and can be called from multiple different location
# def is the keyword to create a function in pyhton

def message(): #This is defining a function
    return"hello world"

# return in the function is not mandatory. If you do not return anything in the funtion it returns none by default

result= message()  #this is the function call
print(result)

# There are several types of  arguments and parameters in pyhton functions.They are categorized as:
# 1. Positional Arguments
# 2. Default Arguments
# 3. Arbitrary Arguments