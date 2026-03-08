"""
Problem 007: 10 001st Prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.
What is the $10,001$st prime number?
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum


def solve() -> int | str:
    limit = 10001
    count = 2
    prime_count = 0
    while True:
        if is_prime(count):
            prime_count += 1
        
        if prime_count >= limit:
            return count
        
        count += 1



if __name__ == "__main__":
    print(solve())
