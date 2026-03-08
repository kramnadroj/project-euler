"""
Problem 004: Largest Palindrome Product
https://projecteuler.net/problem=004

A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
Find the largest palindrome made from the product of two $3$-digit numbers.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum


def solve() -> int | str:
    a = 99
    b = 99
    potential_answer = 0

    for a in range(999, 99, -1):
          for b in range(999, 99, -1):
               total = a * b
               if is_palindrome(total) == True:
                    if total > potential_answer:
                         potential_answer = total

    return potential_answer
               


if __name__ == "__main__":
    print(solve())
