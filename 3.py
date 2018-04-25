# -*- coding: utf-8 -*-
#3
#算法

#给定一个字符串，找出不含有重复字符的最长子串的长度。
#示例：
#给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
#给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
#给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

    
        return max_length

solution = Solution()
result = solution.lengthOfLongestSubstring("abcabcbb")
print(result)
