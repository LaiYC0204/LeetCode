class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # 如果 k 比 n 大，確保 k 在範圍內

        # nums[:] = nums[n-k:] + nums[:n-k]
        nums = nums[n-k:] + nums[:n-k]

        return nums
    
    def rotate2(self, nums, k):
        n = len(nums)
        k = k % n # 如果 k 比 n 大，確保 k 在範圍內

        for _ in range(k):
            temp = nums.pop()
            nums.insert(0, temp)

        return nums
    
    def GPTrotate(self, nums, k):
        n = len(nums)
        k = k % n  # 如果 k 比 n 大，取模以確保 k 在範圍內
        
        # 反轉整個數組
        nums.reverse()
        
        # 反轉前 k 個元素
        nums[:k] = reversed(nums[:k])
        
        # 反轉剩下的元素
        nums[k:] = reversed(nums[k:])
    
s = Solution()
print(s.rotate2([1,2,3,4,5,6,7], 3))