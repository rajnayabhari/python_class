# Create a decorator which checks the password provided by the user. If the password matches 
# "1234" then the user can access the function else show message "your password is invalid"

def login_required(func):
    def inner_func(*args,**kwargs):
        result= func(*args,**kwargs)
        a=(input("enter your password:"))
        if a==1234:
            return  func(*args,**kwargs)
        else:
            return "Your password is invalid"
    return inner_func

@login_required
def add(a,b):
    return a+b

print(add(2,3))