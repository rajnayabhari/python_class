def addition(a,b):
    return a+b

print(addition(2,3))
# here addition is a user called function

class student:
    def age_after_ten_years(self, current_age):
        return current_age+10
student1=student()
age_after_ten_years=student1.age_after_ten_years(10)
print(age_after_ten_years)
# here age_after_ten_years ia s method of class student which can be called using student object

