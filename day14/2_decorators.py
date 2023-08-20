# Decorators are the functions that add extra functionality to the exixting function
# eg:
def decorate_me(func):
    def inner_func():
        print("I am the extra functionality")
        return func()
    return inner_func


@decorate_me
def message():
    print("Hello world")
message()

# message=decorate_me(message)##yesari lekhnu ra @decorate_me lekhnu same ho 
#  #yeasari garda message ma paila ko function na bhai inner function bata passs bhako value aunxa


