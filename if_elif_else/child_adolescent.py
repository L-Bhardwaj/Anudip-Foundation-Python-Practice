# Check if a person is a child, adolescent, or adult based on age

age=int(input("Enter your age: "))
if age>=18:
    print('Adult')
elif age>=13:
    print('Adolescent')
else:
    print("Child")