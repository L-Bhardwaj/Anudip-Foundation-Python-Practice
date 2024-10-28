# Check if a number is a two-digit number or not.

num=int(input('Enter the number: '))
div=num//2
if div<=9 and div>0:
    print(num, ' is a two-digit number.')
else:
    print(num,' is not a two-digit number.')
    