# Determine if a given number is positive, and if it is, check if it’s a two-digit or three-digit number

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    if 10 <= num <= 99:
        print("It is a two-digit number.")
    elif 100 <= num <= 999:
        print("It is a three-digit number.")
    else:
        print("It has more than three digits or less than two.")
else:
    print("The number is not positive.")