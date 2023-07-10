def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
num = int(input("Enter an integer: "))
if num % 2 != 0:
    fact = factorial(num)
    num_digits = len(str(fact))
    print("Factorial of", num, ":", fact)
    print("Number of digits in factorial:", num_digits)
else:
    if is_palindrome(num):
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")
