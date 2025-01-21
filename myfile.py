def find_largest(numbers):
    largest = -99999  # Logical error: Assuming numbers are always non-negative
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def find_smallest(numbers):
    smallest = 99999  # Logical error: Assuming numbers are always non-negative
    for num in numbers:
        if num > smallest:
            smallest = num
    return smallest

# Testing the function
numbers = [-10, -20, -3, -5]
print("The largest number is:", find_largest(numbers))
print("The smallest number is:", find_smallest(numbers))