import sys
sys.path.append('../helpers')

import unittest
import helpers
help = helpers.Helpers()

class TestHelperFunctions(unittest.TestCase):

    def test_input_validity_of_isprime(self):
        self.assertRaises(TypeError, help.is_prime, 'a')
    
    def test_positivity_handling_of_isprime(self):
        self.assertRaises(ValueError, help.is_prime, -1)

    def test_correctness_of_isprime(self):
        self.assertEqual(help.is_prime(3), True)
        self.assertEqual(help.is_prime(4), False)

if __name__ == '__main__':
    unittest.main()