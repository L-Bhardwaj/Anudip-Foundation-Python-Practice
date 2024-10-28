# Check if a string is non-empty, and if so, verify if it contains more than 10 characters

string=input('Enter the String: ')
if string=='':
    print("You entered an Empty String.")
else:
    print('You entered a non-empty String.')
    if len(string)>=10:
        print('And the length of hte string is greater than 10.')