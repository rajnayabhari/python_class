# range()
# range() function can take upto 3 parameters 
# syntax: range(start,end, step_size)
# "end" parameter is always exclusive

data=range(6)#[0, 1, 2, 3, 4, 5]
print(list(data))
print(list(range(0,6)))#[0, 1, 2, 3, 4, 5]

data=range(2,7)
print(list(data))#[2, 3, 4, 5, 6]


data=range(2,10,2)
print(list(data)) #[2, 4, 6, 8]


# enumerate()
# In c and c++ loopin is done in the index of an array
#unlike c or c++ ,looping is done in the element of list/array
#  But in python we can use enumerate to get to get the index in each iteration

vowels=["a","e","i","o","u"]
print(enumerate(vowels))
data=list(enumerate(vowels))
print(data)

for index,value in enumerate(vowels):
    print(index)#0,1,2,3,4
    print(value)#a,e,i,o,u

# for counting from one instead of 0
for index,value in enumerate(vowels,start=1):
    print(index) #1,2,3,4,5
    print(value)#a,e,i,o,u

