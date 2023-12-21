def fib(n):
    dp = [-1] * (n + 1)
    for i in range(1, n + 1):
        if i == 1 or i ==2:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fib(10))