# membership operations

# Dictionary membership is checked in keys an not in values
student = {"name": "john", "age": 25}
print("john" in student)  # false
print("name" in student)  # true
print("age" not in student)  # false

####### Built-in function########
student = {"name": "john", "age": 25}
# Len
print(len(student))  # 2

# sorted()
result = sorted(student)
print(result)  # ["age","name"]

# str
result = str(student)
print(result)  # "{"name":john,"age":25}"

# all(sequence)
# all function only take one parameter and that should be iterable
# All the elements inside the iterable must be truthy for all to return true
data_list = [a, "Hello", [1, 2]]
result = all(data_list)
print(result)  # True

result = all([1, 2, 0])
print(result)  # false because ther is one 0

# But there is one exception is all()
result = all([])
print(result)  # true

# any(sequence)
# any function only take one parameter and that should be iterable
# Any one element inside the iterable must be truthy for any to return true

result = any([1, 0, False])
print(result)  # true
result = any([0, []])
print(result)  # false
