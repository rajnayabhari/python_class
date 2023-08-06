# True or false are the boolean data-types in pyhton. Keywords "True" and "False" are used to represent true state and false state


####### Operation that give boolean type######
#1. comparision
a=5
b=3
print(a>b)#true
print(a<b)#false
print(a==b)#false
print(a>=b)#true
print(a<=b)#false
print(a!=b)#true

#Logical operators
a=5
b=3
print(a>b and b!=a)#true
print(a!=b or a>b) #true


print(not a)#false


#Membership operation
print("a" in ["a","e","i","o","u"])#True
print("i" not in ["a","e","i","o","u"])#false

#Identity operations
a=1
b=1
print(a is b)#True
print(id(a)==id(b))#true
print(a is not b)#false
print(id(a)!=id(b))#false



#### Concept of truthy and falsy####
a=5
print(not a) #False

#Any non-zero or non-empty including True itself is a truthy data-type Eg:5,1,2,-1,[1,2,3,4],(4,5),{-4,-5,"a"},{"a":1},True; all these data are true data types
#In contrast all empty data types, zero,none including False are falsy data tyr
#0,[],{},(),set(),'',Nonr, False are falsy data type.


#How can we verify truthy and falsy
#Check for truthy
a=1
b=[1,2]
c=(1,2)
d={1,2}
e=-4
f={"A":1}
g="Hello world"
h=True
print(bool(a))#True
print(bool(b))#True
print(bool(c))#True
print(bool(d))#True
print(bool(e))#True
print(bool(f))#True
print(bool(g))#True
print(bool(h))#True

#Applying not operation to any truthy value result is false
print(not a) #false

#Check for falsy
a=0
b=[]
c={}
d=()
e=''
f=set()
g=None
h=False

print(bool(a))#False
print(bool(b))#False
print(bool(c))#False
print(bool(d))#False
print(bool(e))#False
print(bool(f))#False
print(bool(g))#False
print(bool(h))#False
print(bool())#False

#Aplying not operations in any falsy value result is true
print(not a)
print(not None)



######Python boolean is sub class of integer#####
#True is integer 1 and False is integer 0

print(True+1)#2
print(70*False)#0
print(True+True)#2
print(False+False)#0