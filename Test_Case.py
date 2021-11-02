from Klargest import Raihan
import unittest


class TestSum(unittest.TestCase):
    
    arr = [3, 8, 12, 1, 5, 36]

    def test_k_less_than_size_arr(self):
        self.assertListEqual(Raihan.get_k_largest(self.arr, 2), [36, 12], "Should be the same")

    def test_k_bigger_than_size_arr(self):
        self.assertListEqual(Raihan.get_k_largest(self.arr, 7), [3, 8, 12, 1, 5, 36], "Should be the same")

if __name__ == '__main__':
    unittest.main()