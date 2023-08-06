#we can d string formatting using f-string

programming_language=input("Enter a language")
message=f"I am learning {programming_language}"
print(message)

name="john doe"
age=20

message=f"i am {name} and i am{age} years old"
print(message)


print('i am %s and i am %d years old' %(name,age))

print('i am {}'.format(name))

