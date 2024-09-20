class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump = 0
        n = len(nums)
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            current_end = max(current_end, nums[i] + i)

            if i == farthest:
                farthest = current_end
                jump += 1
            
        return jump


s = Solution()
print(s.jump([2,3,0,1,4]))