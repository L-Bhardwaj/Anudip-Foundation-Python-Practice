#  Verify if a year is a leap year, and if so, check if it is divisible by 100 and 400

year=int(input('Enter the year: '))
if year%100==0:
    if year%400==0:
        print('It is a leap year.')
    else:
        print('It is not a leap year')
else:
    if year%4==0:
        print(year,' is a leap year.')
    
    