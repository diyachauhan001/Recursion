def sum_of_n_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_n_numbers(n - 1)
    
n = 5
print(f"The sum of the first {n} natural numbers is: {sum_of_n_numbers(n)}")
