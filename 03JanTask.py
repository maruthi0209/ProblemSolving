def is_harshad_number(number):
    """Check if the given number is a Harshad number."""
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(number))
    
    # Check divisibility
    if number % digit_sum == 0:
        return True
    else:
        return False

# Input from the user
number = int(input("Enter a number: "))

# Check and print the result
if is_harshad_number(number):
    print(f"Yes, {number} is a Harshad number.")
else:
    print(f"No, {number} is not a Harshad number.")
