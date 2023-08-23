# Each operator in python has it's own magic method which is called when the operator is carried out
# Magic methods in python are the special methods created using double underscore.
# __add__(),__null()__,__sub()__,__gt()__ etc are some of the ef of magic operators

a=1
b=2
result=a+b
print(result)

result=a.__add__(b)
print(result)

# So, everytime an operation is carried out a magic method is called
# magic methods are also called dunder method