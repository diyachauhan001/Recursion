def reverse_countdown(n):
    if n <= 0:
        return
    else:
        reverse_countdown(n - 1)
        print(n)

reverse_countdown(5)
