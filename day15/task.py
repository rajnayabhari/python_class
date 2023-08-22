# create a class Person with instance attributes name and age.
# create a method get_details in this class to print name and age
class Person:
    
    def __init__(self, name, age): #this is a constructor
        self.name=name  # instance attribute
        self.age=age # instance attribute

    def description(self):
        return f"i am {self.name} and i am {self.age}years old."
    
class Update(Person):
    def __init__(self, name="raj", age=25,grade="bachelor",occupation="programmer"):
        super().__init__(name, age)
        self.grade=grade
        self.occupation=occupation
    def description(self):
        print(super().description())
        return f"I study in {self.grade} and i work as {self.occupation}"

a=Update()
print(a.description())