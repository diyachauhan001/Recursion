def recursive_insertion_sort(arr, n):
    if n <= 1:
        return arr
    
    recursive_insertion_sort(arr, n - 1)
    
    last = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1
    
    arr[j + 1] = last
    
    return arr

array = [12, 11, 13, 5, 6]

print("Original Array:", array)
sorted_array = recursive_insertion_sort(array, len(array))
print("Sorted Array:", sorted_array)
