# # # print first 20 multiple of 3
# for i in range(1,21):
#     print(i*3)
# # # print first 50 positive even numbers
# count=0
# i=0
# while count!=50:
#     if i%2==0:
#         print(i)
#         count+=1
#     i+=1

# # program to take count input from the user and print equivalent even number
# a=int(input("enter the count:"))
# count=0
# i=0
# while count!=a:
#     if i%2==0:
#         print(i)
#         count+=1
#     i+=1

# wap to delete all the occurenece of a specified character in a given string
# s="All the occurrences of a specified character in a given string"
# input=auta chracter choose garne
# output= choose gareko character bahek aru sabai print huna paryo
s="All the occurrences of a specified character in a given string"
a=input("pick a chracter:")
b=""
for i in s:
    if i.lower()==a.lower():
     continue
    b+=i
print(b)