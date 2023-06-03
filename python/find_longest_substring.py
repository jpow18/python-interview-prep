def find_longest_substring(s: str) -> int:
    max_length = 0
    substring_chars = []
    for letter in s:
        if letter not in substring_chars:
            substring_chars.append(letter)
            if len(substring_chars) > max_length:
              max_length = len(substring_chars)
        else:
            if len(substring_chars) > max_length:
              max_length = len(substring_chars)
            substring_chars.clear()
            substring_chars.append(letter)

    return max_length


string = "abcabcbb"
assert find_longest_substring(
    string) == 3, "Test Case 1 Failed: Incorrect length of longest substring"

string = ""
assert find_longest_substring(
    string) == 0, "Test Case 2 Failed: Incorrect length for empty string"

string = "bbbbbb"
assert find_longest_substring(
    string) == 1, "Test Case 3 Failed: Incorrect length for all repeated characters"

string = "abcdefghijklmnopqrstuvwxyz"
assert find_longest_substring(
    string) == 26, "Test Case 4 Failed: Incorrect length for string with no repeated characters"

string = "abccdefg"
assert find_longest_substring(
    string) == 5, "Test Case 5 Failed: Incorrect length of longest substring with repeated characters in the middle"

print("All test cases passed")