# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/degree-of-an-array/

解题思路:

    首先定义一个存储结构 count_dict: {num: [degree, start, end]}
    num     原数组的数
    degree  该数的度
    start   该数第一次出现的位置
    end     该数出现的最后一次位置

    遍历原数组
    当该数字已经存在于 count_dict 中
    需要将该数的度+1，最后出现的位置 end 设置为当前的遍历索引
    当该数字首次出现在 count_dict 中
    初始化结构，设置度为1，首次出现的位置 start 和最后出现的位置 end 均为当前的遍历索引

    利用 max 和 map 获取 count_dict 中最大的度数 max_degree
    利用 filter 筛选 count_dict 中度数为 max_degree 的子字典 max_nums
    利用 min 和 map 获取 max_nums 中 end - start + 1 的最小值，就为原数组中最短连续子数组
"""

from typing import *


class Solution:
    @staticmethod
    def findShortestSubArray(nums: List[int]) -> int:
        count_dict = {}  # {num: [degree, start, end]}
        for index, num in enumerate(nums):
            if num in count_dict:
                count_dict[num][0] += 1
                count_dict[num][2] = index
            else:
                count_dict[num] = [0, 0, 0]
                count_dict[num][0] = 1
                count_dict[num][1] = index
                count_dict[num][2] = index
        max_degree = max(list(map(lambda x: x[1][0], count_dict.items())))
        max_nums = dict(filter(lambda x: x[1][0] == max_degree, count_dict.items()))
        min_sub_nums_length = min(list(map(lambda x: x[1][-1] - x[1][1] + 1, max_nums.items())))
        return min_sub_nums_length


if __name__ == "__main__":
    print(Solution.findShortestSubArray([1, 2, 2, 3, 1]))
