def check_ascending_order(numbers):
    n = len(numbers)
    for i in range(1, n):
        if numbers[i] < numbers[i-1]:
            return False
    return True
num_elements = int(input("Enter the number of elements in the list: "))
numbers =[]
for i in range(num_elements):
    value = int(input("Enter the value: "))
    numbers.append(value)
is_ascending = check_ascending_order(numbers)
print("Original list:", numbers)
if is_ascending:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
