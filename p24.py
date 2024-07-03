def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], find_max(arr[1:]))

def find_min(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return min(arr[0], find_min(arr[1:]))

array1 = [1, 2, 3, 4, 5]
array2 = [10, 2, 30, 5, 8]

print("Maximum of array1:", find_max(array1))
print("Minimum of array1:", find_min(array1))

print("Maximum of array2:", find_max(array2))
print("Minimum of array2:", find_min(array2))
