# Check if a number is positive, negative, or zero, and further check if it is even or odd

number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")
elif number < 0:
    print("The number is negative.")
    if number % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")
else:
    print("The number is zero.")