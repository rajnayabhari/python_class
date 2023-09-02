#  a function is called from the defination of the same  function then it is called as a recursive function
c=0
def count():
    global c
    print(c)
  
    if c==10:
        return
    c+=1
    count()

count()

# Wap to calculate the factorial of 5 in three ways:
# Normal loop
# Reduce()
# Recursion



# Normal loop:
a= 5
f = 1
for i in range(1, a+ 1):
    f = f * i
print("The factorial of", a, "is", f)

# reduce
from functools import reduce

n = 5
s= reduce(lambda x, y: x * y, range(1, n+1))
print(s)


# recursion
def f(n):
    if n == 1:
        return n
    else:
        return n * f(n-1)

a= 5
print("The factorial of", a, "is", f(n))