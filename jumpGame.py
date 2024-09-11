def jump(nums):
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
        
    return False

print(jump([0]))