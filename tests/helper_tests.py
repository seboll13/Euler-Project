import sys
sys.path.append('../helpers')

import unittest
import helpers
help = helpers.Helpers()

class TestHelperFunctions(unittest.TestCase):
    """Test cases for the helper functions"""

    # IS_PRIME
    def test_input_validity_of_isprime(self):
        self.assertRaises(TypeError, help.is_prime, 'a')
    
    def test_positivity_handling_of_isprime(self):
        self.assertRaises(ValueError, help.is_prime, -1)

    def test_correctness_of_isprime(self):
        self.assertEqual(help.is_prime(3), True)
        self.assertEqual(help.is_prime(4), False)
    

    # IS PYTHAGOREAN TRIPLE
    def test_input_validity_of_is_pythagorean_triple(self):
        self.assertRaises(TypeError, help.is_pythagorean_triple, 'a', 'a', 'a')
    
    def test_pythagorean_triple_params_are_increasing(self):
        self.assertRaises(AssertionError, help.is_pythagorean_triple, 3, 2, 1)
    
    def test_correctness_of_is_pythagorean_triple(self):
        self.assertEqual(help.is_pythagorean_triple(3, 4, 5), True)
        self.assertEqual(help.is_pythagorean_triple(3, 4, 6), False)
    
    # GCD
    def test_input_validity_of_gcd(self):
        self.assertRaises(TypeError, help.gcd, 'a', 'a')
    
    def test_positivity_handling_of_gcd(self):
        self.assertRaises(ValueError, help.gcd, -1, -1)
    
    def test_gcd_when_a_is_zero(self):
        self.assertEqual(help.gcd(0, 1), 0)
    
    def test_gcd_when_b_is_zero(self):
        self.assertEqual(help.gcd(2, 0), 2)
    
    def test_correctness_of_gcd(self):
        self.assertEqual(help.gcd(4, 2), 2)
        self.assertEqual(help.gcd(2, 3), 1)
    
    # LCM
    def test_input_validity_of_lcm(self):
        self.assertRaises(TypeError, help.lcm, 'a', 'a')
    
    def test_positivity_handling_of_lcm(self):
        self.assertRaises(ValueError, help.lcm, -1, -1)
    
    def test_correctness_of_lcm(self):
        self.assertEqual(help.lcm(2, 3), 6)
        self.assertEqual(help.lcm(3, 1), 3)
    

if __name__ == '__main__':
    unittest.main()