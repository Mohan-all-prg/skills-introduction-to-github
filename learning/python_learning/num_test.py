import unittest
from num import add

class TestAddFunction(unittest.TestCase):
    def test_addition_of_two_plus_one_returns_three(self):
        # Call the function
        result = add(2, 1)

        # Expected output
        expected_output =  3

        # Assert the output
        self.assertEqual(result, expected_output)

    def test_addition_of_minus_one_plus_minus_two_returns_minus_three(self):
        result = add(-2,-1)
        expected_output = -3

        self.assertEqual(result,expected_output)

if __name__ == '__main__':
    unittest.main()
