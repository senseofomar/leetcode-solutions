# Iterative Divide (Clean & Simple)

def is_power_of_three(n: int) -> bool:
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

# Using Recursion
def is_power_of_three1(n: int) -> bool:
    if n == 1:
        return True
    if n <= 0 or n % 3 != 0:
        return False
    return is_power_of_three1(n // 3)

# Mathematical Trick (Fastest)
def is_power_of_three2(n: int) -> bool:
    return n > 0 and 1162261467 % n == 0
