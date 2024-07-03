def mean_array(arr):
    def sum_array(arr):
        if not arr:
            return 0
        else:
            return arr[0] + sum_array(arr[1:])
    
    def length_array(arr):
        if not arr:
            return 0
        else:
            return 1 + length_array(arr[1:])
    
    total_sum = sum_array(arr)
    length = length_array(arr)
    
    if length == 0:
        return 0  
    else:
        return total_sum / length

array1 = [1, 2, 3, 4, 5]
array2 = [10, 20, 30]

print(mean_array(array1))
print(mean_array(array2))