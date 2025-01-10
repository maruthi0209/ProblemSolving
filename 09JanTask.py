def count_substring(string, substring):
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)  # Find the start index of the substring
        if start == -1:  # If no more substring is found, break the loop
            break
        count += 1
        start += 1  # Move the start index forward to count overlapping occurrences
    return count

# Input from user
string = input("Enter the string: ")
substring = input("Enter the substring: ")

# Calculate and print the count of substring occurrences
result = count_substring(string, substring)
print(f"The substring '{substring}' occurs {result} times in the string.")


###########################################################

def is_perfect_number(n):
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def count_perfect_numbers(start, end):
    """Count perfect numbers in a given range."""
    count = 0
    for num in range(start, end + 1):
        if is_perfect_number(num):
            count += 1
    return count

# Define the range
start = 1
end = 100

# Count and print perfect numbers
perfect_count = count_perfect_numbers(start, end)
print(f"The count of perfect numbers in the range {start} to {end} is {perfect_count}.")
