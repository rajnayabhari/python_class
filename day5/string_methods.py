#1. capitalize()
message="hello world"
result=message.capitalize()
print(result) #Hello world


# 2. title()
result=message.title()
print(result) #Hello World

# 3. Upper()
result=message.upper()
print(result) #HELLO WORLD

# 4.lower()
result=message.lower()
print(result) #hello world

#5. split()
message="Hello all. I am learning python"
result=message.split()  #calling split without any parameters.It splits with <space> by default
print(result) #["Hello","all.","i","am","learning","python"]


result=message.split("o")
print(result) #['Hell', ' all. I am learning pyth', 'n']


message="Hello, all,I,am,learning,python"
result=message.split(",") 
print(result) #['Hello', ' all', 'I', 'am', 'learning', 'python']



# 6.join()
info=['Hello', ' all', 'I', 'am', 'learning', 'python']
result=" ".join(info)
print(result) #Hello  all I am learning python

# info.join(" ") #It raises error because join() should be called with string object not with list

result="+".join(info)
print(result) #Hello+ all+I+am+learning+python

result=", ".join(info)
print(result) #Hello,  all, I, am, learning, python


# 7.find()
message="Hello world"
result=message.find("w")
print(result) #6. It gives index of the searched item

result=message.find("rld")
print(result) #8

result=message.find("Rld")
print(result) #-1. if string is not found then find returns-1.

search_value="Rld"
result=message.find(search_value.lower())
print(result)#8


search_value="Rld" or "rld"
result=message.lower().find(search_value.lower())
print(result)#8


#replace()
message="hello world"
result=message.replace("hello","Hello")
print(result) #Hello world

