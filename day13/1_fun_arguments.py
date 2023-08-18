# order of the function arguments is important to note
# Arguments are the values passed during function call and parameters are the values tkein in the function
# defination


# Order of the arguments 
# 1. Positional/Compulsory Arguments eg a,b,c #positional argument chai value halnai parxa
# 2. Default Arguments eg b=3,c=4
# 3. Arbitiary Arguments

def addition(a,b,c=10): #here'a' and 'b' are positional aruguments and c is default
    return a+b+c

print(addition(2,3,c=5)) #here c is key word argument

# If we send value in the function call then the default value always gets override.here c=10 is overrided by c=5



# Arbitrary Arguments
# Arbitrary arguments can take random number of elements in the function call. they are like an expandable bucket
def addition(*args): #here args is not important but "*" is mandetory we can replace args with any variable
    print(args)
    print(type (args))
    return sum(args)

print(addition(1,2))
print(addition(1,2,3))
print(addition(1,2,3,4))


def addition(**kwargs): #here kwargs is not important but "**" is mandetory
    print(kwargs)
    print(type(kwargs))
    return sum(kwargs.values())

print(addition(a=1,b=2,c=3))
print(addition(a=1,b=2,c=3,d=4))
print(addition(a=1,b=2,c=3,d=4,e=5))

# Arbitary arguments also have their own order. *args shold always come before than **kwargs

def addition(a,b,c,d=1,e=2,f=3,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(args)
    print(kwargs)
    return a+b+c+d+e+f+sum(args)+sum(kwargs.values())

print(addition(4,5,6,7,8,9,10,11,12,13,p=14,q=15))