def sum_array(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])

array1 = [1, 2, 3, 4, 5]
array2 = [10, 20, 30]

print(sum_array(array1))  
print(sum_array(array2))  
