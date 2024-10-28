# Check if a number is divisible by 4, 6, both, or neither

num=int(input("Enter the number: "))
if num%4==0 or num%6==0:
    print("Number is divisible by both 4 and 6.")
elif num%4==0:
    print('Number is divisible by 4.')
elif num%6==0:
    print('Number is divisible by 6.')
else:
    print('Number is neither divisible by 4 nor 6.')