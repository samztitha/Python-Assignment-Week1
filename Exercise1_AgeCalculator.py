# Exercise 1: Age Calculator
# Author: Samztitha
# This program asks for birth date and calculates age in years, months, and days.

from datetime import datetime

try:
    # Step 1: Take user input
    dob_input = input("Enter your date of birth (DD-MM-YYYY): ")

    # Step 2: Convert to datetime
    birth_date = datetime.strptime(dob_input, "%d-%m-%Y")
    today = datetime.today()

    # Step 3: Calculate age
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust negative values
    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12

    # Step 4: Show result
    print(f" You are {years} years, {months} months, and {days} days old.")

except ValueError:
    print("Please enter date in correct format (DD-MM-YYYY).")
