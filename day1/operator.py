###Operators###
#operators are the symbols in python or in any programing language that carry out arithmetic and logical operations
#operations
#the python operrators are
#1.Arithmetic
#2. Relational Operators
#3. Logical Operators
#4. Membership Operators
#5. Identity OPerators
#6. Assignment OPerators

##Arithmetic Operators##
#1.Addition
a=1
b=2
print(a+b)

#2. Subraction
print(a-b)

#3.Multiplication
print(a*b)

#4.division
print(a/b)
#5.Modulus
a=4
b=2
print(a%b)
#5.exponential
print(a**2)
#floor division(//)
#omits the decimal value from the divison operation and gives floor value
print(3//2)
print(-3//2)


### Comparison Operators###
#,==,<,>,<=,>=,=! are the relational operators
#Relational operators give boolean result (True or False)
a=5
b=3
print(a==b)#fasle
print(a>b)#True
print(a<b)#False
print(a!=b)#True

###Logical operators###
# and,or,not are the logical operators
print(a<b or b!=a)#true
print(a==b and a!=b)#false
print(not True)#false
print(not False)#true


a=5
print(not a)#false

a=0
print(not a)# true here it is using the concept of truthy and falsy  which we will learn later



###Assignmment operators###
#is equal to (=) is the simplest assignment operators
a=2+3
#in the above operation,2 and 3 are added and assigned to a variable'a' using assignment operators

a=1
a=a+1
print(a)
a+=1
# here += is also assignment operators
#similarly -=,/=,*= all exist in similar manner
a=20
a%=2
print(a)




###Membership operators###
#in and "not in" are the membeship operators.We can use membership data type in sequence datatype
print(2 in[1,2,3]) #True
print (3 not in [1,2,3])#false




###Identity operators###
# is and "is not" are the identity operators
a=[1,2,3]
b=a
print(a is b)#true
# here a and b are the same object and lies in same memory location
print(id(a)==id(b)) #true
b=a.copy()
print(a is b)
print(id(a)==id(b))#false
# here a and b have same value but are in different memory location



###Precedence and Associativityt###
# if an operation has multiple operators the precedence defines the order of such operators
# if multiple operators have same precedence then the operation is done based  on associativity
# Normally all the operators have left-right associativity except**
print(2*6/3)#4
#Here multiplication and division have same precedence but the associativity is from left-right.so, multiplication is done first then division
print(2**3**2)#512
# For** associativity is form right-left.so,3**2 is executed first




