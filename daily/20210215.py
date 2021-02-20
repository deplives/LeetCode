# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/max-consecutive-ones/

解题思路:
    二进制数组中只包含 0 和 1
    因此可以把数组变为字符串，然后再按照 '0' 分割为新的数组
    分割的新数组只有两种: 空字符串或只包含数量不等的'1'的字符串
    比如原二进制数组为 [1, 0, 0, 1, 1, 0, 1, 1]
    经过组合为字符串为 '10011011'
    用 '0' 分割为 ['1', '', '11', '11']
    找到最长的字符串就是原二进制数组最大连续 1 的个数
"""

from typing import *


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        return len(max("".join(map(str, nums)).split("0")))


if __name__ == "__main__":
    print(Solution.findMaxConsecutiveOnes([1, 0, 0, 1, 1, 0, 1, 1]))
