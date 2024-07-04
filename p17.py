def fib(n):
    if n < 2:
        return n
        
    dp = [0, 0, 1]
        
    for i in range(2, n + 1):
        dp[0] = dp[1]
        dp[1] = dp[2]
        dp[2] = dp[0] + dp[1]
        
    return dp[2]

n = 5
print(f"The {n}th term of the Fibonacci sequence is: {fib(n)}")
