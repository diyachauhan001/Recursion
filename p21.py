def count_steps_to_zero(number):
    def helper(num, steps):
        if num == 0:
            return steps
        if num % 2 == 0:
            return helper(num // 2, steps + 1)
        else:
            return helper(num - 1, steps + 1)
    
    return helper(number, 0)

# Example usage
print(count_steps_to_zero(14))   
print(count_steps_to_zero(8))    
print(count_steps_to_zero(100))  
