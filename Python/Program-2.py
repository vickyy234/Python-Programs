def is_obtained_from_first_string(first_str, second_str):
    first_str_set = set(first_str)
    second_str_set = set(second_str)
    return second_str_set.issubset(first_str_set)
first_str = input("Enter the first string: ")
second_str = input("Enter the second string: ")
if is_obtained_from_first_string(first_str, second_str):
    print("YES")
else:
    print("NO")
