def product_of_digits(n):
    if n == 0:
        return 0
    elif n < 10:
        return n
    else:
        return (n % 10) * product_of_digits(n // 10)

number = 1234
print(product_of_digits(number))


