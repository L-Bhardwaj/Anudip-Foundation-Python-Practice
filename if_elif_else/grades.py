# Determine a student's grade based on marks (A, B, C, D, F).(marks >=75 grade A, 65-75 grade B, 55-65 grade C, 50-55 grade D otherwise fail) 


score=float(input('Enter your score: '))
if score>=75:
    print('Your grade: A')
elif score>=65:
    print('Your Grade: B')
elif score>=55:
    print('Your Grade: C')
elif score>=50:
    print('Your Grade: D')
else:
    print("Fail!")