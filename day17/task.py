# cerate a class Department with parameters name and number of students.create a method total sudents,which takes object as parameters and return the total
# no of student from all department


class Departmet:
    def __init__(self,no_of_students):
        self.no_of_student=no_of_students 
        

    def total_no_of_students(self,other):
        return self.no_of_student +other.no_of_student
    def __add__(self,other):
        return self.no_of_student+other.no_of_student
    

a=Departmet(20)
b=Departmet(30)
result=a.total_no_of_students(b)
print(result)
    
result=a+b
print(result)