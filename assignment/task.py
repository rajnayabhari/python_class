# 2. Write a Python program to calculate the difference between a given
# number and 17. If the number is greater than 17, return twice the absolute
# difference.
a=int(input("Enter a number:"))
if a>17:
    print((a-17)*2)
else:
 print(a-17)


#  1. Write a Python program that accepts an integer (n) and computes the value
# of n+nn+nnn + …
n=int(input("Enter a number:"))
sum=0
for i in range(1,5):
   sum+=n**i
print(sum)


# wap to check whether input number is prime or not
n=int(input("enter an positive integer:"))
count=0
if n==0 or n==1:
    print(f"{n} is not a prime number.")
else:
    for i in range(2,n):
        if n%i==0:
            count+=1

    if count>2:
        print(f"{n} is not a prime number.")
    else:
        print(f"{n} is a prime number.")