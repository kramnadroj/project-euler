"""
Problem 000: Register Question
https://projecteuler.net/register

A number is a perfect square, or a square number, if it is the square of a positive integer.
For example,  is a square number because    ; it is also an odd square.

The first 5 square numbers are: , and the sum of the odd squares is    .

Among the first 707 thousand square numbers, what is the sum of all the odd squares?
"""

# from __future__ import annotations

import math
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum


def solve() -> int | str:
    total = 0
    for i in range(1, 707001):
        square = i * i
        if square % 2 != 0:  # odd square
            total += square

    return total


if __name__ == "__main__":
    print(solve())
