# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/min-stack/

解题思路:
    本题中的核心问题在于如何获取任意时刻的栈中的最小值
    常规方法有:
        1. 用另一个数据结构存储每一次 push pop 操作后的栈的最小值
        2. 直接在当前栈中记录每次 push pop 操作后的的栈中的最小值
    这里以第二种方法进行解析

    |     |      |     |      |     |      |     |
    |     |      |     |      |     |      |_____|
    |     |      |     |      |     |      |__0__|
    |     | push |     | push |_____| push |__0__|
    |     | ---> |     | ---> |__1__| ---> |__1__|
    |     |  1   |_____|  2   |__2__|  0   |__2__|
    |     |      |__1__|      |__1__|      |__1__|
    |_____|      |__1__|      |__1__|      |__1__|

    核心思路为: 每一次 push(x) 把当前(包含x)栈中最小值(minval)继续 push(minval),
    这样一来把 push 的实际数据 x 和当前栈中的最小元素 minval(打包) 作为整体存放到栈中
    pop 也是同理，每次 pop 需要从栈中依次取出当前栈中的最小元素，和实际需要的数据

    以栈底为起始，奇数位置保存实际的有效数据，偶数位置保存当前位置后(栈底方向)栈中的最小值

    优点:
        1. 仅需要一个栈即可完成，不需要维护额外的数据结构
        2. 在任意 push/pop 操作后，栈顶元素均为此时栈中的最小值,且后期无需对该数据进行维护
    缺点:
        1. 需要双倍的栈空间
"""

from typing import *


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        minval = self.stack[-1] if self.stack and self.stack[-1] < x else x
        self.stack.append(x)
        self.stack.append(minval)

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-2]

    def getMin(self) -> int:
        return self.stack[-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(0)
    stack.push(0)
    stack.pop()
    print(stack.getMin())
