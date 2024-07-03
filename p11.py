def count_steps_to_zero(n, steps=0):
    if n == 0:
        return steps
    elif n % 2 == 0:
        return count_steps_to_zero(n // 2, steps + 1)
    else:
        return count_steps_to_zero(n - 1, steps + 1)

number = 15
print(count_steps_to_zero(number))
