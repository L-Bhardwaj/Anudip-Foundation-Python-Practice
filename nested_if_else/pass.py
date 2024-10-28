# Verify if a student has passed a subject, and if passed, check if they scored distinction (≥ 75)

score=float(input('Enter the score: '))
if score>40:
    print('Student has passed the examination.')
    if score >= 75:
        print("They scored a distinction.")
    else:
        print("They did not score a distinction.")
else:
    print('The student has failed.')