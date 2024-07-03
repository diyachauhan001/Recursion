def reverse_number(n, result=0):
    if n == 0:
        return result
    else:
        return reverse_number(n // 10, result * 10 + n % 10)

number = 1234
print(reverse_number(number))
