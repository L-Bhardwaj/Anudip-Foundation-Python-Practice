# Check if a temperature is hot, warm, or cold. (temp >35 hot , 10-35 warm less than 10 cold) 

temperature=float(input('Enter the temperature (in degree C) : '))
if temperature>35:
    print("Temperature is hot.")
elif temperature>=10:
    print('Temperature is warm.')
else:
    print('Temperature is cold.')