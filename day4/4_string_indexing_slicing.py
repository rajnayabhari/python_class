"""String indexing and slicing is similar to the list
forward indexing starts from 0 and reversing ineding starts fro -1"""

#string indexing
message="hello world"
print(message[0]) #h
print(message[3])#l
print(message[5]) #<space>
print(message[-1]) #d
print(message[-7]) #0
print(message[20]) #It raises:IndexError
print(message[-20])#It raises:Index error



#string slicing
message="hello world"
print(message[:5]) #"Hello"
print(message[0:5]) #"Hello"
print(message[3:])#"lo world" 
print(message[2:7]) #"llo w"
print(message[7:2]) #"" it returns empty string because our indexing is form left to right
print(message[:-3])   #"Hello wo"
print(message[0:-3])  #"Hello wo" 
print(message[-4:])  #"orld"
print(message[-2:-7])  #""
print(message[-7:-2])  #"o wor"
print(message[7:-8])  #""
print(message[-8:7]) #"lo W" 

# message="Hello world"
# message[2]="L" # It raises error because we cannot change the existing item in string as it is immutable
del message #It deletes the string
# del message[2] # It raises error because we cannot change the existing item in string as it is immutable


# Iterating through string
message="Hello world"
for each in message:
    print(each) #"H","e","L","l","o"," ","w","o","r","l","d"

for each in message[5]:
    print(each)