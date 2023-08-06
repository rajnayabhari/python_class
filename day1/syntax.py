#####Identifier###
# Any name of a variable , function or class provided by user is an identifier


# Rules of  naming identifiers in python
# 1. Identifiers are case sensitive i.e. Area and area are two different variables
# 2. Identifiers can't be python keywords
# 3. Identifiers name can be A-Z,a-z,0-9 and _
# 4. but it can't start with digit .1a="hello" 1a is invalid identifier
# 5. we can't use special symbols like @,#,$ as identifiers

####Pyhton statement####
# Each line in a python code is statement
# we can seperate multiple statement in same line using semicolon(;)
# we can also use back-slash (\) for the line contuation
message="Hello world"
message1="Hello"; message2="world"
message="Hello"\
"world"
# Indentation in python is very important to represent a code-block 
# Let's see an if code block in c language
# if(a==1){
#     printf("Hello World")
# }
a=5
b=2
if a==1:
    print("Helloworld")
    if  b==2:
        print("2 is also printed")
        print("this is outside b")
print("This is not in if code block ") 