from math import sqrt

class Helpers:
    def __init__(self):
        pass


    def is_prime(self, n) -> bool:
        """Returns whether a particular #n is a prime or not
        @param n is the number to check for primality"""
        if not isinstance(n, int):
            raise TypeError('Parameter must be an integer.')
        if n < 1:
            raise ValueError('Parameter cannot be negative.')
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    

    def is_pythagorean_triplet(self, a, b, c) -> bool:
        """Returns whether or not a given triplet of numbers is pythagorean, i.e. if a^2+b^2=c^2
        @param a,b,c is the proposed triplet"""
        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
            raise TypeError('Parameters must be integers.')
        assert(a < b < c)
        return a**2 + b**2 == c**2
    
    
    def gcd(self, a, b) -> int:
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
    

    def lcm(self, a, b) -> int:
        """Returns the least common multiple between a and b"""
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('Parameters must be integers.')
        if a < 0 or b < 0:
            raise ValueError('Parameters cannot be negative.')
        return (a * b) / self.gcd(a, b)

        