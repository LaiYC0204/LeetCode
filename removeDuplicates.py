def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    output = set()
    j = 0
    for i in range(len(nums)):
        if nums[i] not in output:
            nums[j] = nums[i]
            j += 1
        output.add(nums[i])
    return len(output)

nums = [4,1,2,5,4,1,3,2]
print(removeDuplicates(nums))
print(nums)