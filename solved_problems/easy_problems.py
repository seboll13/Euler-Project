import sys
sys.path.append('../helpers')

import helpers

from time import time
from math import prod,sqrt
from functools import reduce

help = helpers.Helpers()

NB_ITERATIONS = 1_000_000

# Timer decorator
def timer(func):
    """Decorator to time a function"""
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        start = time()
        rv = func(*args, **kwargs)
        end = time()
        print(f'Elapsed time: {(end-start):.3f} [s]') # time in seconds
        #print('Elapsed time: {:.3f} [ms]'.format((end-start)*1000)) # time in milliseconds
        return rv
    return wrapper


class EasyProblems:
    def __init__(self) -> None:
        pass


    # PROBLEM 1
    @timer
    def sum_of_multiples_of_three_and_five(self, n):
        """Returns the sum of all multiples of 3 and 5 below n"""
        return sum((_ for _ in range(n) if _%3 == 0 or _%5 == 0))


    # PROBLEM 2
    @timer
    def even_fibonacci(self, n):
        """Returns the sum of all even fibonacci numbers up to n"""
        fib_arr = [1, 1]
        while fib_arr[-1] < n:
            fib_arr.append(fib_arr[-1]+fib_arr[-2])
        return sum(list(filter(lambda _: _ % 2 == 0, fib_arr)))


    # PROBLEM 3
    @timer
    def largest_prime_factor(self, n):
        """Returns the largest prime factor of a given number n"""
        assert n > 0
        factors = []
        max_range = int(sqrt(n))
        for i in range(2, max_range):
            if n % i == 0:
                factors.append(i)
                n /= i
        return max(factors)
    

    # PROBLEM 4
    @timer
    def largest_palindrome_product(self):
        """Returns the largest palindrome made from the product of two 3-digit numbers"""
        return max([i*j for i in range(100, 1000) for j in range(100, 1000) if str(i*j)[::-1]==str(i*j)[::1]])


    # PROBLEM 5
    @timer
    def smallest_multiple(self, n):
        """Returns the smallest positive number that is evenly divisible by all of the numbers from 1 to n"""
        res = 1
        for i in range(2, n+1):
            if help.is_prime(i):
                res *= int(i * int((n-1)/i))
        return res


    # PROBLEM 6
    @timer
    def sum_square_difference(self, n):
        """Returns the difference between the sum of the squares of the first n natural numbers and the square of the sum"""
        r = range(1, n+1)
        return abs(sum(_ ** 2 for _ in r) -  sum(r)**2)
    
    
    # PROBLEM 7 - TODO: work on niceness
    @timer
    def get_prime(self, idx: int) -> int:
        """Returns the idx-th prime number"""
        assert(idx > 0)
        if idx == 1:
            return 2
        cnt: int = 1
        n: int = 1
        while cnt < idx:
            n += 2
            if help.is_prime(n): cnt += 1
        return n
    

    # PROBLEM 8
    @timer
    def largest_product_in_series(self, num, num_digits) -> int:
        """Returns the largest product of num_digits consecutive digits in num"""
        prods = []
        for i in range(0, len(num)-num_digits):
            prods.append(prod(int(num[i+j]) for j in range(num_digits)))
        return max(prods)
    

    # PROBLEM 9
    @timer
    def find_pythagorean_triplets(self) -> int:
        """Find the product of the pythagorean triplet where a+b+c=1000"""
        gen = ((a,b,c) for a in range(1000) for b in range(1000) for c in range(1000) if a < b and b < c and a+b+c == 1000)
        for a,b,c in gen:
            if help.is_pythagorean_triple(a,b,c):
                return a*b*c
        return -1
    

    # PROBLEM 10
    @timer
    def sum_primes_below(self, upper_bound) -> int:
        """Sum of primes below upper_bound"""
        primes = (_ for _ in range(3, upper_bound, 2) if help.is_prime(_))
        return 2 + reduce(lambda x,y: x+y, primes) # works as fast using the sum() function
    

    # PROBLEM 11
    @timer
    def largest_product_in_grid(self, grid, num_numbers) -> int:
        """Find the largest product of num_numbers numbers in a grid"""
        max_prod = 0
        # horizontal
        for i,el in enumerate(grid):
            for j in range(len(el)-num_numbers):
                max_prod = max(max_prod, prod(el[j:j+num_numbers]))
        # vertical
        for i in range(len(grid)-num_numbers):
            for j in range(len(grid[i])):
                max_prod = max(max_prod, prod(grid[i+k][j] for k in range(num_numbers)))
        # diagonal
        for i in range(len(grid)-num_numbers):
            for j in range(len(grid[i])-num_numbers):
                max_prod = max(max_prod, prod(grid[i+k][j+k] for k in range(num_numbers)))
        # anti-diagonal
        for i in range(len(grid)-num_numbers):
            for j in range(len(grid[i])-num_numbers):
                max_prod = max(max_prod, prod(grid[i+k][j-k] for k in range(num_numbers)))
        return max_prod
    

    # PROBLEM 12
    @timer
    def highly_divisible_triangular_number(self, n) -> int:
        """Returns the first triangular number with more than n divisors"""
        for tn in help.get_triangular_numbers(n):
            if help.get_number_of_factors(tn) > 500:
                return tn
        return -1


    # PROBLEM 13
    @timer
    def large_sum(self) -> str:
        """Sums the first 10 digits of the sum of the numbers in the file"""
        return str(sum(help.read_large_numbers()))[:10]


    # PROBLEM 14
    @timer
    def longest_collatz_sequence(self, upper_bound) -> int:
        """Returns the number under upper_bound that produces the longest Collatz sequence"""
        max_len, max_num = 0, 0
        for i in range(3, upper_bound, 2):
            _, _len = help.generate_collatz_sequence(i, 0)
            if _len > max_len:
                max_len = _len
                max_num = i
        return max_num
    

    # PROBLEM 15
    @timer
    def lattice_paths(self, n) -> int:
        """Compute the number of paths in an n x n grid"""
        return int(help.factorial(2*n) / (help.factorial(n)**2))
    

    # PROBLEM 16
    @timer
    def power_digit_sum(self, n) -> int:
        """Compute the sum of the digits of 2^n"""
        return sum(int(_) for _ in str(2**n))
    

    # PROBLEM 17
    @timer
    def number_letter_counts(self, n) -> int:
        """Compute the number of letters in the numbers 1 to n, ignoring the spaces"""
        return sum(len(help.number_to_english(_).replace(' ', '')) for _ in range(1, n+1))


if __name__ == '__main__':
    ep = EasyProblems()
    print(ep.number_letter_counts(1000))