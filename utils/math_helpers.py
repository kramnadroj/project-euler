"""General math utilities."""
from __future__ import annotations

from math import gcd

def isqrt(n):
    if n < 0:
        raise ValueError("Square root not defined for negative numbers")
    if n == 0:
        return 0
    x = int(n**0.5)
    # correct for floating point imprecision
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b."""
    return a * b // gcd(a, b)


def digits(n: int) -> list[int]:
    """Return the digits of n as a list."""
    return [int(d) for d in str(n)]


def digit_sum(n: int) -> int:
    """Return the sum of digits of n."""
    return sum(digits(n))


def is_palindrome(n: int | str) -> bool:
    """Return True if n is a palindrome."""
    s = str(n)
    return s == s[::-1]


def divisors(n: int) -> list[int]:
    """Return all divisors of n in sorted order."""
    result = set()
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result)


def sum_of_divisors(n: int) -> int:
    """Return the sum of proper divisors of n (all divisors excluding n)."""
    return sum(d for d in divisors(n) if d != n)
