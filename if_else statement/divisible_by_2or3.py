# Check if a number is divisible by both 2 and 3 or not

num=int(input("Enter the number: "))
if num%2==0 or num%3==0:
    print(num,' is divisible by 2 or 3.')
else:
    print(num,' is not divisible by 2 or 3.')
    