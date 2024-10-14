import unittest
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ht = {0: 0, 1: 0, 2: 0}
        for num in nums:
            ht[num] += 1

        i = 0
        for k, v in ht.items():
            for _ in range(v):
                nums[i] = k
                i += 1


class TestSortColor(unittest.TestCase):
    def setUp(self):
        self.test_data_1 = [2, 0, 2, 1, 1, 0]
        self.test_data_2 = [2, 0, 1]
        self.test_data_1_output = [0, 0, 1, 1, 2, 2]
        self.test_data_2_output = [0, 1, 2]

    def test_inputs(self):
        Solution().sortColors(self.test_data_1)
        self.assertEqual(self.test_data_1, self.test_data_1_output)
        Solution().sortColors(self.test_data_2)
        self.assertEqual(self.test_data_2, self.test_data_2_output)
