#  Check if a number is divisible by 2, and if so, further check if it is divisible by 4

num=int(input("Enter the number: "))
if num%2==0:
    print('The number is divisible by 2.')
    if num%4==0:
        print('The number is divisible by 4 as well.')
    else:
        print('But the number is not divisible by 4.')