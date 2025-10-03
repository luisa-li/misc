"""Sum of square of primes, and how many were summed."""

import numpy as np 
from itertools import combinations

def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False

def primes(lowest, highest):
    return [prime for prime in range(1, highest) if is_prime(prime) and prime > lowest]

def squared_primes(lowest, highest):
    return [prime**2 for prime in primes(lowest, highest)]

def sums_of_items(items, k):
    combs = combinations(items, k)
    sums = [sum(comb) for comb in list(combs)]
    return sums 

def compute():
    squares = squared_primes(10, 40)

    for i in range(7):
        print(np.mod(np.array(sums_of_items(squares, i + 1)), 8))
    
if __name__ == "__main__":
    compute()