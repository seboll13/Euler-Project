import helpers
import math

help = helpers.Helpers()

# PROBLEM 1
def sum_of_multiples_of_three_and_five(n):
    s = 0
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            s += i
    return s

# PROBLEM 2
def even_fibonacci(n):
    fib_arr = [1, 1]
    while fib_arr[-1] < n:
        fib_arr.append(fib_arr[-1]+fib_arr[-2])
    return sum(list(filter(lambda x: x % 2 == 0, fib_arr)))

# PROBLEM 3
def largest_prime_factor(n):
    assert n > 0
    factors = []
    max_range = int(math.sqrt(n))
    for i in range(2, max_range):
        if n % i == 0:
            factors.append(i)
            n /= i
    return max(factors)


if __name__ == '__main__':
    # 600851475143
    print(largest_prime_factor(600851475143))