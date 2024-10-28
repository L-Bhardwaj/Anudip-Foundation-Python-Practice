# Determine if a person is employed, and if yes, check their salary range (low, medium, high)
i=input("Are ypu Employed? (Y or n): ").lower()
if i=='y':
    salary=int(input('Enter your Salary: '))
    if salary>2500000:
        print("high Salary.")
    elif salary>1000000:
        print('Medium Salary.')
    else:
        print('Low Salary.')

