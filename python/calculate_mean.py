# Calculate mean of array of floats
def calculate_mean(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    
    sum = 0
    for number in numbers:
        sum += number
        
    return sum / len(numbers)
    

numbers = [1, 2, 3, 4, 5]
assert calculate_mean(numbers) == 3.0, "Test Case 1 Failed"

numbers = [-10, 0, 10]
assert calculate_mean(numbers) == 0.0, "Test Case 2 Failed"

numbers = [1.5, 2.75, 3.25, 4.9]
assert calculate_mean(numbers) == 3.1, "Test Case 3 Failed"

numbers = []
assert calculate_mean(numbers) == 0.0, "Test Case 4 Failed"

numbers = [1000000, 2000000, 3000000, 4000000, 5000000]
assert calculate_mean(numbers) == 3000000.0, "Test Case 5 Failed"

print("All test cases passed")