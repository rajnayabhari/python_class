# Condition are used to make decision in a program
# There are 4 varieties of condition we can create
# 1. simole if
# 2. if...else condition
# 3. if...elif....else ladder
# 4. nested if


# In the if condition ,the statement after the"if" is checked . If the statement is truthy then the
# condition is satisfied and the block of code inside the "if" is executed.otherwise ,it is npt executed
a=20
if a>15:
    print("the number is greater than 15")

if a:
    print(f"the number is {a}")


 # if..else
a=20
if a > 15:
    print("the number is greater than 15")
else:
    print("the number is smaller than 15")

if a:
    print(f"the number is {a}")

else:
    print("The number is 0")

# if..elif..else
exam_mark=76
if(exam_mark>=80):
    print("Scored distinction")

elif exam_mark>=65:
    print("scored first division")

elif exam_mark>=55:
    print("scored second division")

elif exam_mark>=40:
    print("scored third division")

else:
    print("Failed")



# nested if


a=20

if a>10:
    if a>15:
        print(f"{a} is greater than 15")
    else:
        print(f"{a}is just greater than 10")
else:
    print(f"{a} is less than 10)")

# ternary if
# one-liner condition are called ternery if
a=10
b=5
if a>b:
    print("a is greater than b")
else:
    print("b is greaterr")

# ternary if program
print("a is greater") if a>b else print("b is greater")