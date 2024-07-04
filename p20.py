def count_zeros(number):
    def helper(num, count):
        if num == 0:
            return count
        if num % 10 == 0:
            count += 1
        return helper(num // 10, count)
    
    if number == 0:
        return 1
    return helper(number, 0)


print(count_zeros(102030))  
print(count_zeros(0))       
print(count_zeros(12345))   
