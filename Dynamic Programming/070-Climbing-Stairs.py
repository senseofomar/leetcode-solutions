# Dynamic Programming (Iterative)

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n  # base cases: 1->1, 2->2

    a, b = 1, 2  # a = ways(1), b = ways(2)
    for _ in range(3, n + 1):
        a, b = b, a + b  # like Fibonacci
    return b
