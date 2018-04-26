# -*- coding: utf-8 -*-
#7
#算法

#给定一个 32 位有符号整数，将整数中的数字进行反转。
#示例 1:
#输入: 123
#输出: 321
#示例 2:
#输入: -123
#输出: -321
#示例 3:
#输入: 120
#输出: 21
#注意:
#假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        #方法1，耗时较短
        if x > 0:
            sign = 1
        elif x < 0:
            sign = -1
        elif x == 0:
            return 0
        result = str(sign*x)[::-1]
        int_result = int(result)
        if int_result >= 2**31:
            return 0
        else:
            return int_result * sign

        #方法2，耗时较长
        '''
        if x > 0:
            sign = 1
        elif x < 0:
            sign = -1
        elif x == 0:
            return 0
        result = str(sign*x)[::-1]
        int_result = int(result)
        return int_result * sign * (int_result < 2**31)
        '''

solution = Solution()
result = solution.reverse(-123)
print(result)
