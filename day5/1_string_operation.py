# Concatenation #We can concatenate using "+" operator

m1="Hello"
m2="world"
print(m1+m2) #Helloworld



#Repetation / Broadcast operation=> Broadcast in string is doen by using "*"operators
message="Hello"
print(message*3) #HelloHelloHello


#Membership operation
print("m" in "message") #True
print("e"not in "message") #false



###Built_in functions#
# 1. len()= It gives thr lrngth(total no of elements) of sequential data trpes i.e list,string,tuple

message="Hello world"
print(len(message)) #11

#2. type()= returns the type of any object
print(type(message)) #<class "str">

#3. slice()= this function is similar to list and string slicing
sliced_data=slice(2,7)
print(message[sliced_data])#"llo w"