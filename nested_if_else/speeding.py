# Verify if a car is speeding, and if yes, check if it’s above the legal limit by more than 10 km/h

speed = float(input("Enter car speed in km/h: "))
legal_limit = 70
if speed > legal_limit:
    print("The car is speeding.")
    if speed > legal_limit + 10:
        print("The car is speeding excessively.")
else:
    print("The car is within the legal speed limit.")