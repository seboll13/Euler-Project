import math

class Helpers:
    def __init__(self):
        pass

    def is_prime(self, n):
        """Returns whether a particular #n is a prime or not"""
        if not isinstance(n, int):
            raise TypeError('Parameter must be an integer.')
        if n < 1:
            raise ValueError('Parameter cannot be negative.')
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    def gcd(self, a, b):
        """Returns the greatest common divisor of a and b"""
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('Parameters must be integers.')
        if a < 0 or b < 0:
            raise ValueError('Parameters cannot be negative.')
        if a == 0:
            return 0
        if b == 0:
            return a
        return self.gcd(b, b % a)

    def lcm(self, a, b):
        """Returns the least common multiple between a and b"""
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('Parameters must be integers.')
        if a < 0 or b < 0:
            raise ValueError('Parameters cannot be negative.')
        return (a * b) / self.gcd(a, b)

        