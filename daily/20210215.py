# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/max-consecutive-ones/
"""

from typing import *


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        return len(max("".join(map(str, nums)).split("0")))


if __name__ == "__main__":
    print(Solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1, 1]))
