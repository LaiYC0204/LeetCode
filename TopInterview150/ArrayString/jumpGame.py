class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)    
        farthest = 0

        for i in range(n):
            if i > farthest:
                return False

            farthest = max(farthest, nums[i] + i)

            if farthest >= n - 1:
                return True

s = Solution()
print(s.canJump([2,3,1,1,4]))