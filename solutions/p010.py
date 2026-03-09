"""
Problem 010: Summation of Primes
https://projecteuler.net/problem=10

<p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
<p>Find the sum of all the primes below two million.</p>
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum


def solve() -> int | str:
    total = 2000000
    return sum(sieve(total))


if __name__ == "__main__":
    print(solve())
