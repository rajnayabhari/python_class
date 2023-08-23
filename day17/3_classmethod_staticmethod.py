# class methods are the methods which takes class as the first parameter rather than self.
# class method is created using @classmethod decorator
# static methods are the methods which neither takes class nor self as parameter
# they are like normal function which doesnt change the state of the class
# static method is created using @staticmethod decorator


class Student:
    def __init__(self,age):
        self.age=age
        
        
    @classmethod
    def from_birth_year(cls,year):
        age=2023-year
        return cls(age)
    @staticmethod
    def institution_name():
        return "broadway"

s1=Student(25)
print(s1.age)
s2=Student.from_birth_year(1992)
print(s2.age)
print(s2.institution_name())

# Here from_birh_year method is a class method. And it is also sometimes termed as "Factory method"


