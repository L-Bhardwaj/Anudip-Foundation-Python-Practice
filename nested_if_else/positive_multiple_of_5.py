# Check if a number is positive, and if yes, further check if it is a multiple of 5.

num=float(input("enter the number: "))
if num>0:
    print(num, ' is a positive number.')
    if num%5==0:
        print('It is a multiple of 5 as well.')
else:
    print('The number is not positive number.')