"""
Problem 014: Longest Collatz Sequence
https://projecteuler.net/problem=14

<p>The following iterative sequence is defined for the set of positive integers:</p>
<ul style="list-style-type:none;">
<li>$n \to n/2$ ($n$ is even)</li>
<li>$n \to 3n + 1$ ($n$ is odd)</li></ul>
<p>Using the rule above and starting with $13$, we generate the following sequence:
$$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$</p>
<p>It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.</p>
<p>Which starting number, under one million, produces the longest chain?</p>
<p class="note"><b>NOTE:</b> Once the chain starts the terms are allowed to go above one million.</p>
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.primes import sieve, is_prime, prime_factors
from utils.math_helpers import divisors, is_palindrome, digit_sum


def solve() -> int | str:
    
    largest_count = 0
    biggest_number = 0
    for i in range(13, 1000000):
        new_i = i
        count = 1
        while new_i != 1:
            if new_i % 2 == 0:
                new_i = even_rule(new_i)
            else:
                new_i = odd_rule(new_i)
                
            count +=1
            
        if count > largest_count:
            largest_count = count
            biggest_number = i
            
    return biggest_number
                
            
def even_rule(n: int) -> int:
    return n / 2

def odd_rule(n: int) -> int:
    return (3 * n) + 1


if __name__ == "__main__":
    print(solve())
