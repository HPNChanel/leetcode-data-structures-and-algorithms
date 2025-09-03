
def climbStairs(n: int) -> int:
    MAX_SIZE = 50
    dp = [0] * (MAX_SIZE + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, MAX_SIZE + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

"""Hướng giải:
Với bài toán tìm cách leo bậc thang này, nó hoạt động theo quy luật dãy số Fibonacci, tức F(n) = F(n - 1) + F(n - 2)"""
