# Check if a password is correct, and if not, determine if it is due to incorrect characters or length.
password = input("Enter the password: ")
correct_password = "mypassword"
if password == correct_password:
    print("Password is correct.")
else:
    if len(password) != len(correct_password):
        print("Incorrect password length.")
    else:
        print("Incorrect password characters.")