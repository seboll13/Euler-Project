import math

class Helpers:
    def __init__(self):
        pass

    def is_prime(self, n):
        if not isinstance(n, int):
            raise TypeError('Parameter must be an integer')
        if n < 1:
            raise ValueError('Parameter cannot be negative')
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
        