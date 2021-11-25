import math

class Helpers:
    def __init__(self):
        pass

    def is_prime(self, n):
        assert isinstance(n, int)
        assert n > 0
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True
        