#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return n
        # 使用字典储存之前的变量
        # O(n) 时间复杂度, O(n) 空间复杂度
        # adict = {}
        # adict[1] = 1
        # adict[2] = 2
        # for i in range(3, n+1):
        #     adict[i] = adict[i-1] + adict[i-2]
        # return adict[i]

        # 优化，只需存储前两次的结果再相加
        # O(n) 时间复杂度, O(1) 空间复杂度
        x, y= 1, 2
        for i in range(3, n+1):
            answer = x + y
            x = y
            y = answer

        return answer


# 虽同为 O(n) 时间复杂度，但第一种比第二种更快一点点，可能是因为不用赋值
# @lc code=end

