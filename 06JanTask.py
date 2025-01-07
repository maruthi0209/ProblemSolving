# Question 1
def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nearest_primes(number):
    """Find the nearest prime number(s) to the given number."""
    lower, upper = number - 1, number + 1

    # Find the nearest prime below the number
    while lower > 1 and not is_prime(lower):
        lower -= 1

    # Find the nearest prime above the number
    while not is_prime(upper):
        upper += 1

    # Return both if equidistant, else the closest one
    if abs(number - lower) == abs(number - upper):
        return lower, upper
    elif abs(number - lower) < abs(number - upper):
        return lower,
    else:
        return upper,

# Input from the user
number = int(input("Enter a number: "))

# Find and print the nearest prime(s)
result = nearest_primes(number)
print("Nearest prime number(s):", " ".join(map(str, result)))

##########################################################################################

# Question 2
def is_prime_digit(digit):
    """Check if a single digit is a prime number."""
    return digit in {2, 3, 5, 7}

def sum_of_prime_digits(number):
    """Calculate the sum of prime digits in the given number."""
    digits = [int(digit) for digit in str(number)]
    prime_digits = [digit for digit in digits if is_prime_digit(digit)]
    return sum(prime_digits)

# Input from the user
number = int(input("Enter number: "))

# Calculate and print the sum of prime digits
result = sum_of_prime_digits(number)
print(f"The sum of prime digits in {number} is: {result}")
