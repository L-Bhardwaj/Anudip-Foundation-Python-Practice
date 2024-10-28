# Check if a number is divisible by 3, and if yes, further check if it’s divisible by 9.

number = int(input("Enter a number: "))
if number % 3 == 0:
    print("The number is divisible by 3.")
    if number % 9 == 0:
        print("It is also divisible by 9.")
    else:
        print("It is not divisible by 9.")
else:
    print("The number is not divisible by 3.")