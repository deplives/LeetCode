# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/toeplitz-matrix/


解题思路:
    所谓的 托普利茨矩阵 本质就是
    上一行去掉最后一个元素 == 下一行去掉第一个元素
    那么只需要依次比较相邻两行的内容是否满足上述条件即可
"""

from typing import *


class Solution:
    @staticmethod
    def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
        for lrow, crow in zip([i for i in range(len(matrix))], [j for j in range(1, len(matrix))]):
            if matrix[lrow][:-1] != matrix[crow][1:]:
                return False
        return True


if __name__ == "__main__":
    m = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print(Solution.isToeplitzMatrix(m))
