import sys
sys.path.append('../helpers')

import math
import helpers
help = helpers.Helpers()

class EasyProblems:
    # PROBLEM 1
    def sum_of_multiples_of_three_and_five(self, n):
        s = 0
        for i in range(n):
            if i%3 == 0 or i%5 == 0:
                s += i
        return s

    # PROBLEM 2
    def even_fibonacci(self, n):
        fib_arr = [1, 1]
        while fib_arr[-1] < n:
            fib_arr.append(fib_arr[-1]+fib_arr[-2])
        return sum(list(filter(lambda x: x % 2 == 0, fib_arr)))

    # PROBLEM 3
    def largest_prime_factor(self, n):
        assert n > 0
        factors = []
        max_range = int(math.sqrt(n))
        for i in range(2, max_range):
            if n % i == 0:
                factors.append(i)
                n /= i
        return max(factors)

    # PROBLEM 6
    def sum_square_difference(self, n):
        sum, sum_squares = 0, 0
        for i in range(1, n+1):
            sum_squares += i**2
            sum += i
        return abs(sum_squares - sum ** 2)
    
    # PROBLEM 5 
    def smallest_multiple(self, n):
        res = 1
        for i in range(2, n+1):
            if help.is_prime(i):
                res *= int(i * math.floor((n-1)/i))
        return res


if __name__ == '__main__':
    ep = EasyProblems()
    print(ep.smallest_multiple(20))