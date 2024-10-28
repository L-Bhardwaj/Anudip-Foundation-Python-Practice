# Determine the type of triangle (equilateral, isosceles, or scalene)

angle1=int(input("Enter the first angle: "))
angle2=int(input("Enter the second angle: "))
angle3=int(input("Enter the third angle: "))

if angle1==angle2 and angle2==angle3:
    print('It is an Equilateral Triangle.')
elif  angle1==angle2 or angle2==angle3 or angle3==angle1:
    print('It is an isoscles Triangle.')
elif angle1!=angle2 and angle2!=angle3 and angle3!=angle1:
    print("It is a scalen Triangle.")
else:
    print("It is a Triangle.")