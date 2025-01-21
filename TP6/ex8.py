def safe_division(a, b):
    return a / b

import unittest

class TestDivision(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(10,0)

if __name__ == '__main__':
    unittest.main()