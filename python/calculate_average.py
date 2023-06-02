# Takes list of floats as input,
# returns the average value
def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


numbers = [2, 4, 6, 8, 10]
assert calculate_average(
    numbers) == 6.0, "Test Case 1 Failed: Incorrect average"

numbers = []
assert calculate_average(
    numbers) == 0.0, "Test Case 2 Failed: Incorrect average for empty list"

numbers = [-1, -2, -3, -4, -5]
assert calculate_average(
    numbers) == -3.0, "Test Case 3 Failed: Incorrect average for negative numbers"

numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
assert calculate_average(
    numbers) == 3.5, "Test Case 4 Failed: Incorrect average for decimal numbers"

numbers = [1000000, 2000000, 3000000, 4000000, 5000000]
assert calculate_average(
    numbers) == 3000000.0, "Test Case 5 Failed: Incorrect average for large numbers"

print("All test cases passed")