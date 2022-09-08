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
    def f(*args, **kwargs):
        start = time()
        rv = func(*args, **kwargs)
        end = time()
        print('Elapsed time: {:.3f} [s]'.format(end-start)) # time in seconds
        #print('Elapsed time: {:.3f} [ms]'.format((end-start)*1000)) # time in milliseconds
        return rv
    return f


class EasyProblems:
    def __init__(self) -> None:
        pass


    # PROBLEM 1
    @timer
    def sum_of_multiples_of_three_and_five(self, n):
        return sum((_ for _ in range(n) if _%3 == 0 or _%5 == 0))


    # PROBLEM 2
    @timer
    def even_fibonacci(self, n):
        fib_arr = [1, 1]
        while fib_arr[-1] < n:
            fib_arr.append(fib_arr[-1]+fib_arr[-2])
        return sum(list(filter(lambda _: _ % 2 == 0, fib_arr)))


    # PROBLEM 3
    @timer
    def largest_prime_factor(self, n):
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
        return max([i*j for i in range(100, 1000) for j in range(100, 1000) if str(i*j)[::-1]==str(i*j)[::1]])


    # PROBLEM 5
    @timer
    def smallest_multiple(self, n):
        res = 1
        for i in range(2, n+1):
            if help.is_prime(i):
                res *= int(i * int((n-1)/i))
        return res


    # PROBLEM 6
    @timer
    def sum_square_difference(self, n):
        r = range(1, n+1)
        return abs(sum(_ ** 2 for _ in r) -  sum(r)**2)
    
    
    # PROBLEM 7 - TODO: work on niceness
    @timer
    def get_prime(self, idx: int) -> int:
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
        prods = []
        for i in range(0, len(num)-num_digits):
            prods.append(prod(int(num[i+j]) for j in range(num_digits)))
        return max(prods)
    

    # PROBLEM 9
    @timer
    def find_pythagorean_triplets(self) -> int:
        gen = ((a,b,c) for a in range(1000) for b in range(1000) for c in range(1000) if a < b and b < c and a+b+c == 1000)
        for a,b,c in gen:
            if help.is_pythagorean_triplet(a,b,c):
                return a*b*c
        return -1
    

    # PROBLEM 10
    @timer
    def sum_primes_below(self, upper_bound) -> int:
        primes = (_ for _ in range(3, upper_bound, 2) if help.is_prime(_))
        return 2 + reduce(lambda x,y: x+y, primes) # works as fast using the sum() function


if __name__ == '__main__':
    ep = EasyProblems()
    print(ep.sum_square_difference(NB_ITERATIONS))