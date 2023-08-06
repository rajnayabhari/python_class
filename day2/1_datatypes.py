# Like in another programming language it also has its own datatype
#1. Numbers=>Immutable
# 2.Boolean=>Immutable
# 3.list=>Mutable
# 4.tuple=>Immutable
# 5. string=>Immuatble
# 6.Dictionary=>Mutable
# 7.set=>Mutable

# Three things must be kept in mind while studying dat types
# 1. Operators
# 2. Methods
# 3. Built-in function

# Except numbers and boolean, other data types in python are sequental.
# E.g. List,set,dictionary,tuple and string


#######Mutable and Immutable Objects#####
# If an objects once created can be altered in its lifetime period then its is mutable data type
# Example of mutable objects are list,dictionary, and set.
# If it is not altered it is immutable
# Example of immutable objects are Numbers,Boolean,Tuple and string.
   # program to chack diff between mutable and immutable
a=[1,2,3,4]
a[1]=4 #data is changed because list is mutable
b=(1,2,3,4)
b[1]=4 #error is found because touple is immutable
