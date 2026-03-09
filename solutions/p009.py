"""
Problem 009: Special Pythagorean Triplet
https://projecteuler.net/problem=9

<p>A Pythagorean triplet is a set of three natural numbers, $a b c$, for which,
$$a^2 + b^2 = c^2.$$</p>
<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
<p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p>
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum, isqrt


def solve() -> int | str:
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = a ** 2 + b ** 2
            if c ** 0.5 % 1 == 0:
                c = c ** 0.5
                potential_answer = a + b + c
                print(potential_answer)
                if potential_answer == 1000:
                    return a * b * c
                



if __name__ == "__main__":
    print(solve())
