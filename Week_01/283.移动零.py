#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # 双指针，先把不为0的数提出来，再把后面的值赋为0
        # 两次遍历，时间复杂度为 O(n)，没有新增 空间
        # j = 0
        # for i in xrange(len(nums)):
        #     if nums[i]:
        #         nums[j] = nums[i]
        #         j += 1

        # for i in xrange(j, len(nums)):
        #     nums[i] = 0


        # 借用 快速排序的思想，一次遍历
        # 把不等于 0 的放在左边，为 0 的放在右边
        # 时间复杂度为 O(n)
        j = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1



# @lc code=end

