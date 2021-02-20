# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/remove-element/

解题思路:
    首先要求`就地`删除数组的值，就需要用索引的方式遍历数组，使用 del 删除对应的元素
    但是这样就会有一个问题
    每删除一个元素，原数组的长度已经发生了变化(长度变短)
    当用索引遍历原数组的时候就会出现 IndexError 的异常
    所以就需要用一个 deltimes 存储删除的元素的数量
    每次用 index 遍历数组的时候减这个修正值，保证在删除元素后遍历不会出错
    并在删除元素之后将 deltimes += 1
"""

from typing import *


class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        deltimes = 0
        for index in range(len(nums)):
            index = index - deltimes
            if nums[index] == val:
                del nums[index]
                deltimes += 1
        return len(nums)


if __name__ == "__main__":
    n = [0, 1, 2, 2, 3, 0, 4, 2]
    print(Solution.removeElement(n, 2))
    print(n)
