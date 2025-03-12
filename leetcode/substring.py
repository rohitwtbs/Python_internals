def get_all_substrings(input_string):
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substrings.append(input_string[i:j])
    substrings.sort(key=len, reverse=True)
    return substrings


my_string = "rohitkumar"
all_substrings = get_all_substrings(my_string)
print(all_substrings)