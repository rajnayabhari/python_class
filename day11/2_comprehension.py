squared=[]
# for i in range(1,6):
#     squared.append(i**2)
# print(squared) #1,4,9,16,25

b=[i**2 for i in range(1,6)]
print(b)
# This is example of list comprehension


# dictionary comprehension example
squared_dict={k:k**2 for k in range (1,6)}
print(squared_dict)