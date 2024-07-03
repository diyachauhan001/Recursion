def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = 48
num2 = 18

print(f"The GCD of {num1} and {num2} is:", gcd(num1, num2))
