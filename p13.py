def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 0:
        return power(a * a, b // 2)
    else:
        return a * power(a * a, (b - 1) // 2)

base = 2
exponent = 5
print(f"{base} raised to the power {exponent} is: {power(base, exponent)}")
