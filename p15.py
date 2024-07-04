
def isPowerOfThree(n):
    return n > 0 and 3**19 % n == 0


n = 27
print(f"{n} is a power of three: {isPowerOfThree(n)}")