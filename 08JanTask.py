def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary = str(remainder) + binary
        decimal_number = decimal_number // 2
    return binary

# Input from user
decimal_number = int(input("Enter a decimal number: "))
binary_representation = decimal_to_binary(decimal_number)
print(f"Binary representation of {decimal_number} is: {binary_representation}")

######################################

def sum_of_digits_until_single_digit(number):
    while number >= 10:  # Continue until the number is a single digit
        digit_sum = 0
        while number > 0:
            digit_sum += number % 10  # Add the last digit
            number //= 10  # Remove the last digit
        number = digit_sum  # Update the number to the sum of its digits
    return number

# Input from the user
number = int(input("Enter a number: "))
result = sum_of_digits_until_single_digit(number)
print(f"The single-digit sum of the given number is: {result}")

