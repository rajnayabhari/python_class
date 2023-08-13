# wap to prompt the user for hours and rate per hour using input to compute gross pay.
#  pay the hourly rate for the hours upto 40 and 1.5 times the hourly rate for all hours worked above 40 hrs.

a=float(input("Enter total hours:"))
b=float(input("Enter the rate per hour:"))
if a>40:
    print((a-40)*(b*1.5)+(40*b))
else:
    print(a*b)
 