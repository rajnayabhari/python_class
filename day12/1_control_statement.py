# break,continue and pass are the control statements that can alter the normal flow of the program
for i in range(10):
    if i==4:
        break
    print(i)#0,1,2,3

n=0
while n<=10:
    if n==5:
        break
    print(n)
    n+=1

# continue
for i in range(10):
    if i==5:
        continue
    print(i)

n=0
while n<=10:
    if n==5:
        n+=1 
        continue
    print(n)

# pass
# def addition(a,b):
#     pass#codes come here in future

# class student:
#     pass #codes come here in future 