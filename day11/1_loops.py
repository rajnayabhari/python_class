# Loops are used to execute certain code blocks repeatedly
# They are used to reduce manual efforts in the algorithm.

# for loop in python with different datatypes
vowels=["a","e","i","o","u"]
for each in vowels:
    print(each)

# Looping is similar in list,tuple and set.
# lets,s see how is it done in dictionary

student={"name":"jane","age":25,"address":"KTM"}

# Looping in dictionary keys
print(student.keys())

for key in student.keys():
    print(key)

# Looping in dictionary values
print(student.values())

for values in student.values():
    print(values)


# looping through both dictionary keys and values
print(student.items())

print(student.items())

# for items in student.items():
#     print(items) yo chai name ra jane sangai lyauna lai use garne

for key,values in student.items():
    print(key)
    print(values) #yo chai each element palo pilo lina


# we can also use else in for loop
vowels=["a","e","i","o","u"]
for each in vowels:
    print(each)
else:
    print("This code is executed completely") #else ma rakheko for loop completely run  bhaye paxi
    # matra print hunxa break bhayo bhane print hudaina while ma nih same hunxa