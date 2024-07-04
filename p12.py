def decimal_to_binary(n):
    if n == 0:
        return ''
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

decimal_number = 25
print(f"The binary representation of {decimal_number} is: {decimal_to_binary(decimal_number)}")

