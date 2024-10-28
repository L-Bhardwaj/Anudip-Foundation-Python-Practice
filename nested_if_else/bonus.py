# Determine if an employee is full-time or part-time, and if full-time, check if they are eligible for a bonus

employment_type = input("Are you a full-time or part-time employee? ").lower()
if employment_type == "full-time":
    years_of_service = int(input("Enter your years of service: "))
    if years_of_service > 5:
        print("You are eligible for a bonus.")
    else:
        print("You are not eligible for a bonus.")
else:
    print("You are a part-time employee and not eligible for a bonus.")