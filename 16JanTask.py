def unique_numbers_with_underscores(numbers):
    from collections import Counter
    
    # Count occurrences of each number
    counts = Counter(numbers)
    
    # Build the output string
    result = []
    for num, count in counts.items():
        result.append(f"{num}{'_' * (count - 1)}")  # Add underscores based on duplicates
    
    return " ".join(result)

# Input from the user
numbers = list(map(int, input("Enter N integers separated by space: ").split()))
result = unique_numbers_with_underscores(numbers)
print(f"Output: {result}")


#####################################################

def count_unique_numbers(numbers):
    unique_numbers = set(numbers)  # Convert the list to a set to get unique elements
    return len(unique_numbers)  # Return the count of unique elements

# Input from the user
numbers = list(map(int, input("Enter N integers separated by space: ").split()))
unique_count = count_unique_numbers(numbers)
print(f"Count of unique numbers: {unique_count}")
