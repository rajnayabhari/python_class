# Create a list of first 10 multiple of 3 using list comprehension

range(7)
print(list(range(7)))#[0, 1, 2, 3, 4, 5, 6]

for value in range(7):
    print(value)#0
1
2
3
4
5
6#


#task without list comprhension
a=[]
for i in range(1,11):
    a.append(i*3)
    print(a)#[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# task with list comprehension
a=[i*3 for i in range(1,11)]
print(a)#[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]