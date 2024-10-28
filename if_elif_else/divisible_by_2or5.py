#  Check if a number is divisible by 2, 5, or both.

num=int(input("Enter the number: "))
if num%2==0 or num%5==0:
    print("Number is divisible by both 2 and 5.")
elif num%2==0:
    print('Number is divisible by 2.')
elif num%5==0:
    print('Number is divisible by 5.')
else:
    print('Number is neither divisible by 2 nor 5.')