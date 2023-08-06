# Pyhton list are mutable datatypes and are sequential(also an iterable).
# Lists are created enclosing data in big bracket[] or using built in function list()

# Creating an empty list
a=[]
b=list()

# Creating an non empty list
a=[1,2,3]
vowels=["a","e","i","o","u"]
# The above are the example of list with homogenous data-types

# List can contain heteregenous types
a=[1,2,3,["a","e","i","o","u"],{"a",1},{"a":1,"b":2}] #List with  multiple data type


###### Acessing List Items#####
# List items can be acessed using indexing and slicing

# Indexinig in list starts from 0 for forward traverse and -1 for reverse traverse
vowels=["a","e","i","o","u"]
print(vowels[0])#a
print(vowels[2] ) #i
print(vowels[4]) #u

print(vowels[-1]) #u
print(vowels[-3]) #i

# print(vowels[10]) #Indexerror:List index out of range
# print(vowels[-8]) #Indexerror:List index out of range

# Index assignment is possible in list as it is mutable
vowels[1]="E"
print(vowels)



# List Slicing
a=["a","b","C","d","e","f","g","h","i","j"]
print(a[0:5])#['a', 'b', 'C', 'd', 'e']
print(a[:5]) #['a', 'b', 'C', 'd', 'e']
print(a[2:]) #['C', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(a[2:7]) #['C', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(a[7:2]) #[]

print(a[0: -2])#['a', 'b', 'C', 'd', 'e', 'f', 'g', 'h']
print(a[:-2])#['a', 'b', 'C', 'd', 'e', 'f', 'g', 'h']
print(a[-5:])#['f', 'g', 'h', 'i', 'j']

print(a[-7:2])#[]


#####List operation####

# concatenation
a=[1,2,3,]
b=[4,5,6]
result=a+b
print(result)


# Membership operation
print(2 in [1,2,3])#true
print(3 not in[1,2,3])#false


