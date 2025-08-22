def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

try:
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    if start <= 0 or end <= 0:
        raise ValueError("Numbers must be positive!")

    primes = [str(num) for num in range(start, end+1) if is_prime(num)]

    print("\n Prime numbers:")
    for i in range(0, len(primes), 10):   # 10 numbers per line
        print(" ".join(primes[i:i+10]))

except ValueError as e:
    print(e)
