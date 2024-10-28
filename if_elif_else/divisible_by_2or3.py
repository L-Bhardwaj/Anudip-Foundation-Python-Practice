# Determine if a number is divisible by 2, 3, both, or neither

num=int(input("Enter the number: "))
if num%2==0 or num%3==0:
    print("Number is divisible by both 2 and 3.")
elif num%2==0:
    print('Number is divisible by 2.')
elif num%3==0:
    print('Number is divisible by 3.')
else:
    print('Number is neither divisible by 2 nor 3.')
    