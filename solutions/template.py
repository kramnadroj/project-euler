"""
Problem NNN: <title>
https://projecteuler.net/problem=NNN

<problem statement>
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum


def solve() -> int | str:
    pass


if __name__ == "__main__":
    print(solve())
