"""
Problem 003: Largest Prime Factor

https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum


def solve() -> int | str:
    total = 600851475143
    return(prime_factors(total).pop())

if __name__ == "__main__":
    print(solve())
