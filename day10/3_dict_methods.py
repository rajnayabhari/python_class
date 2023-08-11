# copy()
student = {"name": "John", "age": 35}
student1 = student.copy()
print(student)
print(student1)

# get()
student = {"name": "John", "age": 35}
name = student.get("name")
print(name)  # John

name = student["name"]
print(name)

roll = student.get("roll")  # None
# roll=student['roll'] #Error

roll = student.get('roll', 5)
print(roll)  # 5
name = student.get("name", "jane")
print(name)  # John

# items()
student={"name":"John","age":35}
print(student.items())  # dict_items([('name', 'John'), ('age', 35)])

# keys()
student = {"name": "John", "age": 35}
print(student.keys()) #dict_keys(['name', 'age'])

# values()
student = {"name": "John", "age": 35}
print(student.values())#dict_values(['John', 35])
