# Exercise 2: Prime Number Generator
# This program finds all prime numbers within a user-specified range
# and prints them 10 numbers per line. Includes input validation.

# Function to check if a number is prime
def is_prime(n):
    """Return True if n is a prime number, else False"""
    if n < 2:  # Numbers less than 2 are not prime
        return False
    # Check divisibility from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    # Ask user for starting number of the range
    start = int(input("Enter the start of the range : "))
    
    # Ask user for ending number of the range
    end = int(input("Enter the end of the range : "))

    # Validate inputs
    if start <= 0 or end <= 0:
        raise ValueError("Both numbers must be positive integers.")
    if start > end:
        raise ValueError("Start of range must be less than or equal to end of range.")

    # Generate prime numbers in the range
    primes_num = [str(num) for num in range(start, end + 1) if is_prime(num)]

    # Print primes in formatted output (10 numbers per line)
    print("\nPrime numbers in the range:")
    for i in range(0, len(primes_num), 10):
        print(" ".join(primes_num[i:i + 10]))

except ValueError as e:
    # Handle invalid inputs 
    print(" Input Error:", e)
except Exception as e:
    # Handle any other unexpected errors
    print("Unexpected Error:", e)
