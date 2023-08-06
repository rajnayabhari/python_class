##### We can loop(for loop) through the list in following ways
#Example of discomprehension 
a=[1,2,3,4]
for i in a:
    print(i)

b=[]
for i in a:
    b.append(i**2)
    print(b)
c=[]
for i in a:
    c.append(i+5)
    print(c)
#Example of Comprehension in list-
b=[i**2 for i in a]
print(b)