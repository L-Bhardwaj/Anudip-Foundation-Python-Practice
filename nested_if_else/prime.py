# Verify if a number is within a range, and if it is, check if it is a prime number.

num = int(input("Enter a number: "))
if 1 <= num <= 100:
    print("The number is within the range 1 to 100.")
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("The number is not a prime number.")
                break
        else:
            print("The number is a prime number.")
else:
    print("The number is not within the range 1 to 100.")