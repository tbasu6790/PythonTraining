import unittest
from assignment11 import factorial, is_prime, area_of_circle

class TestMathFunctions(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_is_prime(self):
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-3))

    def test_area_of_circle(self):
        self.assertAlmostEqual(area_of_circle(4), 50.26548245743669, places=5)
        with self.assertRaises(ValueError):
            area_of_circle(0)
        with self.assertRaises(ValueError):
            area_of_circle(-2)

if __name__ == "__main__":
    unittest.main()
