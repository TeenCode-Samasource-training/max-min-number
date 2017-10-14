import unittest
from maxAndMinValues import findMaxMin
class MaxMinTest(unittest.TestCase):
    """docstring for MaxMinTest"""

    def test_find_max_min_four(self):
        self.assertListEqual([1, 4],  findMaxMin([1, 2, 3, 4]))


    def test_find_max_min_identity(self):
        self.assertListEqual([4], findMaxMin([4, 4, 4, 4]))

if __name__ == "__main__":
    unittest.main(exit = False)


