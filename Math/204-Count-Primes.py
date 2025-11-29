# Sieve of Eratosthenes (Best + Fastest)
def count_primes(n: int) -> int:
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p < n:
        if is_prime[p]:
            for i in range(p * p, n, p):
                is_prime[i] = False
        p += 1

    return sum(is_prime)

# Check primes one by one
def count_primes1(n: int) -> int:
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    count = 0
    for i in range(n):
        if is_prime(i):
            count += 1
    return count
