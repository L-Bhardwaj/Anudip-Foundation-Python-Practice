# Assign a performance rating based on a percentage (excellent, good, average, poor).

percentage=float(input("Enter your percentage: "))
if  percentage>=90:
    print('Excellent')
elif percentage>=75:
    print("Good")
elif percentage>=50:
    print('Average')
else:
    print("Poor")
    