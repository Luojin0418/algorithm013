#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        adict = {}

        for i in range(len(nums)):
            
            temp = target - nums[i]
            index = adict.get(temp)
            if (index is not None) and (index != i):
                return [index, i]
            
            adict[nums[i]] = i

        return None

# @lc code=end