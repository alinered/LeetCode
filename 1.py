# -*- coding: utf-8 -*-
#1
#算法

#给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#示例:
#给定 nums = [2, 7, 11, 15], target = 9
#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #第一次解答，当nums元素过多时，执行超出时间限制
        '''
        leng = len(nums)
        for i in range(leng-1):
            for j in range(i+1,leng):
                if nums[i] + nums[j] == target:
                    l = [i, j]
                    break
        return l
        '''

        #第二次解答，参考别人的回答
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
