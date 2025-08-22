from datetime import datetime

try:
    # Ask for birthdate in mm/dd/yyyy format
    birth_input = input("Enter your birth date (mm/dd/yyyy): ")
    
    # Validate and convert to datetime
    birth_date = datetime.strptime(birth_input, "%m/%d/%Y")
    
    # Get today’s date
    today = datetime.today()
    
    # Calculate age
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    print(f" Your current age is: {age} years")
    
    # Convert and display in IST format (dd/mm/yyyy)
    print(" Your birthdate in IST format:", birth_date.strftime("%d/%m/%Y"))

except ValueError:
    print("Invalid date format! Please enter in mm/dd/yyyy format.")
