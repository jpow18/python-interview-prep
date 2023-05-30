# Returns sum of even numbers from given array
def sum_even_numbers(numbers: list[int]) -> int:
    sum = 0
    for number in numbers:
        if (number % 2 == 0):
            sum += number
    return sum

def test_sum_even_numbers():
    # Test Case 1
    assert sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30, "Test Case 1 Failed"

    # Test Case 2
    assert sum_even_numbers([2, 4, 6, 8, 10]) == 30, "Test Case 2 Failed"

    # Test Case 3
    assert sum_even_numbers([1, 3, 5, 7, 9]) == 0, "Test Case 3 Failed"

    # Test Case 4
    assert sum_even_numbers([-2, 0, 2, 4, 6]) == 10, "Test Case 4 Failed"

    # Test Case 5
    assert sum_even_numbers([]) == 0, "Test Case 5 Failed"

    print("All test cases pass")

test_sum_even_numbers()
