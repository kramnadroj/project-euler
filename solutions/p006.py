"""
Problem 006: Sum Square Difference
https://projecteuler.net/problem=6

<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum


def solve() -> int | str:
    limit = 100
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, limit + 1):
        sum_of_squares += i ** 2
        square_of_sum += i

    return square_of_sum ** 2 - sum_of_squares



if __name__ == "__main__":
    print(solve())
