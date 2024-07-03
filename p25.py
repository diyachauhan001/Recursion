def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num1 = 5
num2 = 0

print(f"The factorial of {num1} is:", factorial(num1))  
print(f"The factorial of {num2} is:", factorial(num2))  
