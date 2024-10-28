# Determine if a given year is in the 19th, 20th, or 21st century

year = int(input("Enter a year: "))
if 1801 <= year <= 1900:
    print("19th century")
elif 1901 <= year <= 2000:
    print("20th century")
elif 2001 <= year <= 2100:
    print("21st century")
else:
    print("Out of range")