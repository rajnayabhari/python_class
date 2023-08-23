# create a class circle with aan attribute radius.Create a two objects of c1 and c2.Add the radius of the circle and print the result.
# Do the above task using methos ad then magic method
# compare the size of circle and print the result using magic method.

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def total_radius(self,other):
        return self.radius +other.radius
    def __add__(self,other):
       return self.radius+other.radius
    def __gt__(self,other):
        # if self.radius>other.radius:
        #     return("the c2 radius is greater")
        # else:
        #     return("the c2 radius is greater")
        self.radius>other.radius
        return True



c1=Circle(20)
c2=Circle(30)
result=c1.total_radius(c2)
print(result)
result=c1+c2
print(result)
result=c1<c2
print(result)