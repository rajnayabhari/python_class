import time
# print(time.time())
# create a decorator which calculates the amount of time that it took to execute a function

def calc_execution_time(func):
    start=time.time()
    def inner_func(*args,**kwargs):
        result= func(*args,**kwargs)
        end=time.time()
        print(f"execution time is {end-start}seconds")
        return result
    
    return inner_func   
    
    

@calc_execution_time
def message(txt):
    for i in range(1000000):
        continue
    return txt
print(message("Hello"))

