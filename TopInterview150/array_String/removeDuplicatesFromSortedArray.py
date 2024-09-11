class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        index = 0

        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
                nums[index] = nums[i]
                index += 1

        return len(s)
    
    def otherRemoveDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)
    
s = Solution()
print(s.otherRemoveDuplicates([1,1,2]))