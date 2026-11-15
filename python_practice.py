#first program: print Hello World
print("Hello World")

#second program: add two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)

#third program: simple calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input")
calculator()

#fourth program: maximum of two numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

max_value = max_of_two(10, 20)
print("The maximum of 10 and 20 is:", max_value)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
max_value = max_of_two(num1, num2)
print("The maximum of", num1, "and", num2, "is:", max_value)

#fifth program: check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

#sixth program: factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("The factorial of", num, "is:", factorial(num))

#seventh program: fibonacci series
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_fib = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_fib)
    return fib_series[:n]

num = int(input("Enter the number of terms in Fibonacci series: "))
print("Fibonacci series up to", num, "terms:")

#eighth program: reverse a string
def reverse_string(s):
    return s[::-1]

input_string = input("Enter a string: ")
print("Reversed string:", reverse_string(input_string))

#ninth program: check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(input_string, "is a palindrome.")
else:
    print(input_string, "is not a palindrome.")

#tenth program: find simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
interest = simple_interest(principal, rate, time)
print("Simple interest is:", interest)

#eleventh program: find compound interest
def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
interest = compound_interest(principal, rate, time)
print("Compound interest is:", interest)