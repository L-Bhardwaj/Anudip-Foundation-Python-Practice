# Check if a month belongs to a season (spring, summer, fall, winter)

month = input("Enter the month: ").lower()
if month in ["march", "april", "may"]:
    print("Season: Spring")
elif month in ["june", "july", "august"]:
    print("Season: Summer")
elif month in ["september", "october", "november"]:
    print("Season: Fall")
else:
    print("Season: Winter")