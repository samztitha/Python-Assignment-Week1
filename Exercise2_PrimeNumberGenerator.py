# Exercise 2: Prime Number Generator
# Author: Samztitha
# Program generates prime numbers within a given range.

def is_prime(num: int) -> bool:
    """Check if number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    # Step 1: Input range
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    if start <= 0 or end <= 0:
        print(" Only positive integers allowed.")
    elif start > end:
        print("Start must be less than end.")
    else:
        # Step 2: Generate primes
        primes = [n for n in range(start, end + 1) if is_prime(n)]

        # Step 3: Display results
        print(f"Prime numbers between {start} and {end}:")
        print(primes if primes else "None found")

except ValueError:
    print("Invalid input. Please enter integers only.")
