def find_unique_elements(given_list):
    unique_list = []
    for element in given_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Basic Input
numbers = [2, 4, 2, 6, 8, 4, 10]
assert find_unique_elements(numbers) == [2, 4, 6, 8, 10], "Test Case 1 Failed"

# Empty list
numbers = []
assert find_unique_elements(numbers) == [], "Test Case 2 Failed"

# All elements are unique
numbers = [1, 2, 3, 4, 5]
assert find_unique_elements(numbers) == [1, 2, 3, 4, 5], "Test Case 3 Failed"

# No Unique Elements
numbers = [1, 1, 1, 1, 1]
assert find_unique_elements(numbers) == [1], "Test Case 4 Failed"

# Negative and positive numbers
numbers = [2, -4, 2, -6, 8, 4, -10]
assert find_unique_elements(numbers) == [
    2, -4, -6, 8, 4, -10], "Test Case 5 Failed"

print("All test cases passed")