"""
Problem 005: Smallest Multiple
https://projecteuler.net/problem=5

<p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
<p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum


def solve() -> int | str:
    limit = 20
    smallest_potenatial_answer = limit
    success = False

    while True:
        for i in range(limit, 0, -1):
            if smallest_potenatial_answer % i != 0:
                break
            elif i == 1:
                success = True
                break

        if success:
            return smallest_potenatial_answer
        
        smallest_potenatial_answer += limit



if __name__ == "__main__":
    print(solve())
