import unittest
from calc import aec_divide

# python -m unittest -v tests/test_subtract.py

class TestDivide(unittest.TestCase):
    def test_divide(self):
        arg_ints = [10,2]
        sub_result = aec_divide(arg_ints)
        self.assertEqual(sub_result, 5)

    def test_denom_cant_be_zero(self):
        arg_ints = [10, 0]
        sub_result = aec_divide(arg_ints)
        self.assertEqual(sub_result, 0)

    def test_arg_length(self):
        arg_ints = [10, 1, 2]
        self.assertRaises(Exception, aec_divide, arg_ints)

if __name__ == "__main__":
    unittest.main()
