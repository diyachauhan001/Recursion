def isPowerOfFour(n):
    return n > 0 and bin(n).count('1') == 1 and (n - 1) % 3 == 0


n = 16
print(f"{n} is a power of four: {isPowerOfFour(n)}")