def print_triangle(A):

    if len(A) < 1:
        return
    
    temp = [0] * (len(A) - 1)
    for i in range(len(A) - 1):
        x = A[i] + A[i + 1]
        temp[i] = x
    
    print_triangle(temp)
    
    print(A)

A = [1, 2, 3, 4, 5]
print_triangle(A)
