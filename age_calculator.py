from datetime import date


year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))

# Today's date
today = date.today()

# Calculate age in years
age = today.year - year


if today.month < month or (today.month == month and today.day < day):
    age -= 1

print("You are " + str(age) + " years old.")
