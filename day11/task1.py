# wap to take 3 number input and print the greatest
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>b and a>c:
    print(f"{a} is the greatest no")
elif b>a and b>c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest") 