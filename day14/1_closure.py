#  closure is the concept in python which fulfills the following:
# 1.There should be a nested function (afunction inside another function)
# 2. An innner function must reference the argument from outer function
# 3. Outer function should return the inner function

def closure_fxn(messg):
    def inner_fxn():
        print(messg)
    return inner_fxn
result=closure_fxn("Hello World")
result()  #yo call na gare sama inner function run hundaina result=inner function  garya jasto matra hunxa
# The above function is the simplest closure that can be made in python.
# closure are the base of decorators in python