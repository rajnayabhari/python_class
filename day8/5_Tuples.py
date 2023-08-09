#Tuples are immutable data-types. They are sequential data types
# Elements in tuple are enclosed in parenthesis (small bracket)


# Creating an empty tuple
a=tuple()
print(a) #empty tuple
a=()
print(a) #empty tuple

#Creating a non-empty tuple
a=(1,2,3)
print(a)

a=tuple([1,2,3])
print(a)
a=([1,3],1,"a",{"1":2})
print(a)

a=1
print(type(a)) #int

a=(1,)
print(a) #=> Tuple
a=1,
print(type(a)) #tuple
