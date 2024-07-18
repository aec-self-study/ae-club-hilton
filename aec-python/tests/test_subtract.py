import unittest
from calc import aec_subtract

# python -m unittest -v tests/test_subtract.py

class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        arg_ints = [20,5]
        sub_result = aec_subtract(arg_ints)
        self.assertEqual(sub_result, 15)
    
    def test_cant_go_below_zero(self):
        arg_ints = [5, 20]
        sub_result = aec_subtract(arg_ints)
        self.assertEqual(sub_result, 0)
    
    def test_arg_length(self):
        arg_ints = [10, 1, 2]
        self.assertRaises(Exception, aec_subtract, arg_ints)

if __name__ == "__main__":
    unittest.main()
