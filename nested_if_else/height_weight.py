# Verify if a person’s height is above 160 cm, and if yes, check their weight category (underweight, normal, overweight)

height = float(input("Enter your height in cm: "))
if height > 160:
    weight = float(input("Enter your weight in kg: "))
    if weight < 50:
        print("You are underweight.")
    elif 50 <= weight <= 80:
        print("You have a normal weight.")
    else:
        print("You are overweight.")
else:
    print("Your height is 160 cm or below.")