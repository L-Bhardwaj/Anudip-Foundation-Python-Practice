# Determine a person’s life stage (child, teen, adult, senior) based on age

age=int(input('Enter your age: '))
if age>=60:
    print("Life's Stage: Senior")
elif age>=18:
    print("Life's Stage: Adult")
elif age>=13:
    print("Life's Stage: Teen")
else:
    print("Life's Stage: Child")

