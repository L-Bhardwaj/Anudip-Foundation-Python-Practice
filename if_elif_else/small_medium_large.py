# Determine if a number is small, medium, or large (range-based).(number > 10000 large,100-10000 medium, less than 100 small) 

num=int(input("Enter the number: "))
if num>10000:
    print("Large")
elif num>100:
    print("Medium")
else:
    print('Small')
    