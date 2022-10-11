from math import sqrt
from typing import Generator

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
    

    def read_grid(self) -> list:
        """Reads the grid file and returns a list of lists of integers"""
        with open('../files/grid11.txt', 'r') as f:
            return [[int(num) for num in line.split(' ')] for line in f.readlines()]
    

    def get_number_of_factors(self, n) -> int:
        """Returns a list of all factors of a given number n"""
        if not isinstance(n, int):
            raise TypeError('Parameter must be an integer.')
        if n < 1:
            raise ValueError('Parameter cannot be negative.')
        num_factors = 0
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                num_factors += 1
                if i != n/i:
                    num_factors += 1
        return num_factors


    def get_triangular_numbers(self, n):
        """Generates the first n triangular numbers"""
        if not isinstance(n, int):
            raise TypeError('Parameter must be an integer.')
        if n < 1:
            raise ValueError('Parameter cannot be negative.')
        return (n*(n+1)//2 for n in range(1, n+1))
    

    def read_large_numbers(self):
        """Reads the large numbers file and returns a list of integers"""
        with open('../files/largenums13.txt', 'r') as f:
            return (int(line) for line in f.readlines())
    

    def generate_collatz_sequence(self, n, cnt) -> tuple:
        """Generates the collatz sequence for a given number n"""
        if n == 1:
            return (1, cnt)
        if n % 2 == 0:
            return self.generate_collatz_sequence(int(n/2), cnt+1)
        return self.generate_collatz_sequence(3*n + 1, cnt+1)
    

    def factorial(self, n):
        """Returns the factorial of a given number n"""
        if not isinstance(n, int):
            raise TypeError('Parameter must be an integer.')
        if n < 1:
            raise ValueError('Parameter cannot be negative.')
        if n == 1:
            return 1
        return n * self.factorial(n-1)
    

    def numbers_to_19(self) -> list:
        return ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    

    def tens(self) -> list:
        return ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    

    def number_to_english(self, n) -> str:
        """Returns the english representation of a given number n"""
        if not isinstance(n, int):
            raise TypeError('Parameter must be an integer.')
        if n < 1:
            raise ValueError('Parameter cannot be negative.')
        if n < 20:
            return self.numbers_to_19()[n]
        if n < 100:
            return self.tens()[n//10] + ('' if n % 10 == 0 else ' ' + self.number_to_english(n % 10))
        if n < 1000:
            return self.numbers_to_19()[n//100] + ' hundred' + ('' if n % 100 == 0 else ' and ' + self.number_to_english(n % 100))
        if n < 1000000:
            return self.number_to_english(n//1000) + ' thousand' + ('' if n % 1000 == 0 else ' ' + self.number_to_english(n % 1000))
        if n < 1000000000:
            return self.number_to_english(n//1000000) + ' million' + ('' if n % 1000000 == 0 else ' ' + self.number_to_english(n % 1000000))
        return self.number_to_english(n//1000000000) + ' billion' + ('' if n % 1000000000 == 0 else ' ' + self.number_to_english(n % 1000000000))
        