# Dynamic Programming (Iterative)

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n  # base cases: 1->1, 2->2

    a, b = 1, 2  # a = ways(1), b = ways(2)
    for _ in range(3, n + 1):
        a, b = b, a + b  # like Fibonacci
    return b


# Recursion with Memoization

def climb_stairs2(n: int, memo={}) -> int:
    if n <= 2:
        return n
    if n in memo:
        return memo[n]
    memo[n] = climb_stairs2(n-1, memo) + climb_stairs2(n-2, memo)
    return memo[n]
