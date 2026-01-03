def get_all_substrings(input_string):
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substrings.append(input_string[i:j])
    substrings.sort(key=len, reverse=True)
    return substrings

def palindrome(str):
    left = 0
    right = len(str) - 1
    while left <right:
        if (str[left] != str[right]):
            return False
        left += 1
        right -= 1
    return True


string = "qqqqqqqwqwwqdqwdqwerqwerjqrjqrjqjrjeqrjeqrjqjrqdddddbabad"
all_substrings = get_all_substrings(string)

for substring in all_substrings:
    if palindrome(substring):
        print(substring)
        break