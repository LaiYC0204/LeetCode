class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        index = 0

        for i in range(len(nums)):
            d.setdefault(nums[i], 0)
            if d[nums[i]] < 2:
                d[nums[i]] += 1
                nums[index] = nums[i]
                index += 1

        return index
    
    def GPTremoveDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        index = 2
        
        for i in range(2, len(nums)):
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1
        
        return index
    
s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))