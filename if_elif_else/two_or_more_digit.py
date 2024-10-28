# Check if a number is one-digit, two-digit, or more

num=int(input('Enter the number: '))
num=str(num)
if len(num)>2:
    print('more')
elif len(num)==2:
    print('Two Digit')
else:
    print('One Digit')