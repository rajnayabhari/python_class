# Poltmorphism in python refers to many forms of the same functions or objects.
# sum(),len(),max(),min() etc. They are some of the examples which follows polymorphism.
# These bilt-in functions can take different datatypes and perform their respective tasks.

# There are two important aspects  of polymorphism:
# 1. Function/Method Overloading
# 2. Operator Overloading

# Function/Method overloading

def addition(a,b):
    return a+b

def addition(a,b,c):
    return a+b+c

# result=addition(1,2)  #It raises type error
# print(result)
result=addition(1,2,3)
print(result)

# though addition is defined twice only the latest defination is considered. so python doesn't support function overloading




# But we can give default argument so that we can pass both two and three arguments in the function call
def addition(a,b,c=0):
    return a+b+c
result=addition(1,2)
print(result)
result=addition(1,2,3)
print(result)



class Employee:
    salary=1200

    def descripiton(self):
        return self.salary
    
    def description(self):
        return f"salary is{self.salary}"
    

e=Employee()
print(e.descripiton())  #The last defination is considered so the result is salary is 1200