# 
# Determine if a given time is morning, afternoon, or evening

hour = int(input("Enter hour (0-23): "))
if 5 <= hour < 12:
    print("Morning")
elif 12 <= hour < 18:
    print("Afternoon")
else:
    print("Evening")